select DATE_PART('month',rental_date) as rental_month 
	  ,DATE_PART('year',rental_date) as rental_year
	  ,i.store_id as store_id
	  ,count(distinct rental_id) as count_rentals
from inventory i
join rental r 
on i.inventory_id=r.inventory_id
GROUP BY 1,2,3
ORDER BY 4 DESC