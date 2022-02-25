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
	  ,full_name
	  ,count(payment_id) as pay_countpermon
	  ,sum(p.amount) as monthly_amount
	  ,sum(p.amount) - lag(sum(p.amount)) over (partition by full_name order by date_trunc('month',payment_date)) as monthly_change
from payment as p
join top_10_cust as c
on p.customer_id=c.customer_id
group by 1,2
order by 2,1

					 