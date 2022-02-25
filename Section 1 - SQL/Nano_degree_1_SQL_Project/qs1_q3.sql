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
where category_name IN ('Animation','Children','Classics','Comedy','Family','Music')
GROUP BY 1,2
ORDER BY 1,2

	