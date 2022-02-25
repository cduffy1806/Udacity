/* Q1: How have our top customer cohort performed MoM? */

with top_10_cust as (select c.customer_id
						,first_name
						,last_name
						,first_name || ' ' || last_name full_name
						, sum(amount) as amount
					from customer c
					join payment p
					on c.customer_id=p.customer_id
					GROUP BY 1,2,3,4
					ORDER BY 5 DESC
					LIMIT 10
					 )
select date_trunc('month',payment_date) as pay_month
	  ,count(payment_id) as pay_countpermon
	  ,sum(p.amount) as monthly_amount
	  ,sum(p.amount) - lag(sum(p.amount)) over (order by date_trunc('month',payment_date)) as monthly_change
from payment as p
join top_10_cust as c
on p.customer_id=c.customer_id
group by 1
order by 1

/* Q2: Store Performance by Rental Order */
select to_char(rental_date,'YYYY-MM') as rental_month
	  ,i.store_id as store_id
	  ,count(distinct rental_id) as count_rentals
from inventory i
join rental r
on i.inventory_id=r.inventory_id
GROUP BY 1,2
ORDER BY 3 DESC

/* Q3: Music Category Rental Duration v Average */
with ranked_duration as (select f.title film_title
							  ,c.name as category_name
							  ,f.rental_duration as rental_duration
							  ,NTILE(4) OVER (ORDER BY rental_duration ASC) as standard_quartile
						FROM film f
						LEFT JOIN film_category fc
						on f.film_id=fc.film_id
						LEFT JOIN category c
						on fc.category_id=c.category_id
						ORDER BY rental_duration)
select category_name
	   ,standard_quartile
	   ,COUNT (*) as count
from ranked_duration
where category_name IN ('Music')
GROUP BY 1,2
ORDER BY 1,2

/* Q4: Most Popular “Family Friendly” Films to Rent		*/
SELECT film_title,
	   category_name,
	   COUNT (*) as rental_count
FROM
		(select f.title film_title
			  ,c.name as category_name
		 	  ,r.rental_id as rental_id
		FROM film f
		LEFT JOIN film_category fc
		on f.film_id=fc.film_id
		LEFT JOIN category c
		on fc.category_id=c.category_id
		JOIN inventory i
		on f.film_id=i.film_id
		JOIN rental r
		on i.inventory_id=r.inventory_id
		where c.name IN ('Animation','Children','Classics','Comedy','Family','Music')) t1
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 10
