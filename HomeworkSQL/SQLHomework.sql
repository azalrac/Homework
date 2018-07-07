use sakila;
Select *
from actor;

--1a
Select first_name, last_name
from actor;

--1b
Select CONCAT(first_name, ' ', last_name) as 'Actor Name'
from actor;

--2a
Select first_name, last_name
from actor
where first_name = 'Joe';

--2b. Find all actors whose last name contain the letters `GEN`:
Select first_name, last_name
from actor
where last_name like '%GEN%';

--2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
Select first_name, last_name
from actor
where last_name like '%LI%'
order by last_name, first_name;

--2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
Select country_id
from country
where country in ('Afghanistan', 'Bangladesh', 'China');

--3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(50) AFTER first_name;

Select *
from actor;

--3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.
Alter TABLE actor MODIFY COLUMN middle_name blob;

--3c. Now delete the `middle_name` column
Alter TABLE actor drop column middle_name;

--4a. List the last names of actors, as well as how many actors have that last name.
Select last_name, count(actor_id) as 'number of actors'
from actor
group by last_name;

--4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
Select last_name, count(*) as 'num_of_actors' from actor group by last_name having count(actor_id) >1

--4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

Select *
from actor 
where last_name = 'williams' and first_name = 'GROUCHO';

update actor
set first_name = 'HARPO'
where last_name = 'williams' and first_name = 'GROUCHO';

--confirm change
Select *
from actor 
where last_name = 'williams';

--4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, 
--if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what 
--the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)

Select *
from actor 
where last_name = 'williams' and first_name = 'HARPO';

update actor
set first_name = 'MUCHO GROUCHO'
where last_name = 'williams' and first_name = 'HARPO';

--confirm change
Select *
from actor 
where last_name = 'williams';

--5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
SHOW CREATE TABLE actor;

--6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:

Select s.first_name, s.last_name, a.address
from staff s
JOIN address a 
on (s.address_id = a.address_id);

--6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.

--Select * from staff;
--Select * from payment;

Select s.first_name, s.last_name, sum(p.amount) as 'Amount'
from staff s
JOIN payment p 
on (s.staff_id = p.staff_id)
where  payment_date between '2005-01-01' and '2005-12-31'
group by s.first_name, s.last_name;

--Need to verify above query

--6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
SELECT f.title, count(a.actor_id) as 'Number of Actors'
FROM film_actor a
INNER JOIN film f ON f.film_id = a.film_id
group by f.title;

--6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
Select count(inventory_id) as 'Copies of Hunchback Impossible'
from inventory 
where film_id in (
Select film_id
from film
where title = 'Hunchback Impossible')
group by film_id;

--* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
Select c.first_name, c.last_name, sum(p.amount) as 'Total Amount Paid'
from customer c
join payment p on p.customer_id = c.customer_id
group by c.last_name
order by c.last_name;

--7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 

Select title from film where left(title,1) in ('K','Q')
and language_id in (
Select language_id
from language
where name = 'English');

--7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
Select first_name, last_name
from actor 
where actor_id in (
Select actor_id
from film_actor
where film_id in (
Select film_id
from film
where title = 'Alone Trip'));

--7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
--Select * from customer;  customer_id, address_id
--Select * from address;  address_id, city_id
--Select * from city;      city_id, country_id
--Select * from country;  country_id, country

Select cu.first_name, cu.last_name, cu.email
from country c
join city on city.country_id = c.country_id
join address a on city.city_id = a.city_id
join customer cu on cu.address_id = a.address_id
where c.country = 'Canada'

--amother solution
Select first_name, last_name, email from customer
where address_id in (
Select address_id
from address where city_id in (
Select city_id from city where country_id in (
Select country_id from country where country = 'Canada')));

--7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
Select title from film where film_id in (
select film_id from film_category where category_id in (
Select category_id from category where name = 'Family'))

--7e. Display the most frequently rented movies in descending order.
--select * from rental  rental_id, inventory_id
--select * from inventory  inventory_Id, film_id
--select * from film  title, film_id

Select f.title as 'Movie', count(r.rental_id) as 'Rentals'
from film f
join inventory i on i.film_id = f.film_id
join rental r on r.inventory_id = i.inventory_id
group by f.title
order by Rentals desc;

--7f. Write a query to display how much business, in dollars, each store brought in.
--Select * from payment;    amount  rental_id
--Select * from rental;     rental_id  & inventory_id
--select * from inventory;  inventory_id & store_id
--Select * from store;   store_id

Select i.store_id, sum(p.amount) as 'Total Amount Received'
from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id = i.inventory_id
group by i.store_id


--7g. Write a query to display for each store its store ID, city, and country.
--Select * from store   store_id & address_id
--Select * from address  address_id & city_id
--select * from country  country_id & country
--Select * from city city_id & country_id

Select s.store_id, city.city, c.country
from address a
join city on city.city_id = a.city_id
join country c on c.country_id = city.country_id
join store s on s.address_id = a.address_id

--7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
--Select * from category   category_id & name(genre)
--Select * from film_category  film_id & category_id
--select * from inventory   inventory_id, film_Id
--select * from payment      rental_id, amount
--select * from rental        rental_id, inventory_id

Select c.name as 'Genre', sum(p.amount) as 'Revenue'
from category c
join film_category fc on c.category_id = fc.category_id
join inventory i on i.film_id = fc.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by c.name
order by revenue desc limit 5;


--8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

CREATE VIEW `top_5_genre` AS 
Select c.name as 'Genre', sum(p.amount) as 'Revenue'
from category c
join film_category fc on c.category_id = fc.category_id
join inventory i on i.film_id = fc.film_id
join rental r on r.inventory_id = i.inventory_id
join payment p on p.rental_id = r.rental_id
group by c.name
order by revenue desc limit 5;

--8b. How would you display the view that you created in 8a?

Select * from top_5_genre;

--8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
drop view top_5_genre;
