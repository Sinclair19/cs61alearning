.read data.sql


CREATE TABLE average_prices AS
  SELECT category, SUM(MSRP)/COUNT(*) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;

CREATE TABLE best_deal AS
  SELECT p.name AS name, MIN(p.MSRP/p.rating) FROM products AS p GROUP BY p.category;

CREATE TABLE shopping_list AS
  SELECT b.name, l.store FROM lowest_prices AS l, best_deal AS b WHERE b.name = l.item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(s.Mbs) FROM stores AS s, shopping_list AS l WHERE l.store = s.store;

