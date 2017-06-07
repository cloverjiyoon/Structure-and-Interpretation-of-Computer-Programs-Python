create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from parents, dogs where name = parent order by -height;

-- Sentences about siblings that are the same size
create table sentences as
  with siblings(s1, s2) as (
      select a.child, b.child from parents as a, parents as b 
        where a.parent = b.parent and a.child < b.child
    )
  select s1 || " and " || s2 || " are " || a.size || " siblings"
    from siblings, size_of_dogs as a, size_of_dogs as b
      where  a.name = s1 and b.name = s2 and a.size = b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with add_height(t_names, total_height, max, n) as (
      select name, height, height, 1 from dogs union
      select t_names || ", " || name, total_height + height, height, n + 1
        from add_height, dogs where n < 4 and max < height
    )
  select t_names, total_height from add_height where n = 4 and total_height >= 170 
        order by total_height;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  select a.n as num, count(*) as div from ints as a, ints as b 
    where a.n % b.n = 0 group by a.n;
    
create table primes as
    select num from divisors where div = 2;
