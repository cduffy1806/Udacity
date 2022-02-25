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
select DATE_TRUNC('month',payment_date) as pay_month 
	  ,full_name
	  ,count(payment_id) as pay_countpermon
	  ,sum(p.amount) as monthly_amount
from payment p
join top_10_cust c
on p.customer_id=c.customer_id
GROUP BY 1,2
ORDER BY 2,1

					 