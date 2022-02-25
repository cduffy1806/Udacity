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
ORDER BY category_name 
		,film_title
	