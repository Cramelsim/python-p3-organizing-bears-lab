select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT bears.name
    FROM bears
    ORDER BY bears.name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT bears.name, bears.age
    FROM bears
    WHERE alive = 1
    ORDER BY bears.age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age
    FROM bears
    ORDER BY bears.age DESC
    LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age
    FROM bears
    ORDER BY bears.age ASC
    LIMIT 1;
"""

select_most_prominent_color_and_returns_with_count = """
    SELECT bears.color, COUNT(bears.color) as count
    FROM bears
    GROUP BY bears.color
    ORDER BY count DESC
    LIMIT 1;
"""

counts_number_of_bears_with_goofy_temperaments = """
    SELECT COUNT(*)
    FROM bears
    WHERE temperament = 'goofy';
"""

select_bear_that_killed_Tim = """
    SELECT *
    FROM bears
    WHERE temperament = 'aggressive' AND color = 'black' AND name IS NULL;
"""