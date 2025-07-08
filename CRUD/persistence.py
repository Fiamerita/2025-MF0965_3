from db import get_connection


class CustomerRepository:
    def fetch_all(self):
        query = """
        SELECT Code, Name, Population
        FROM world.country;
          FROM customer c
          JOIN address a     ON c.address_id = a.address_id
          JOIN city    city  ON a.city_id = city.city_id;
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def delete(self, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
        conn.commit()
        cursor.close()
        conn.close()

    # métodos add(id), update(id), etc.
