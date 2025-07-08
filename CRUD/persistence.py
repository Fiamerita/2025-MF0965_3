from db import get_connection


class CustomerRepository:
    def fetch_all(self):
        query = """
SELECT   
    country.Code, 
    country.Name, 
    country.Population,
    city.Name AS Capital,
    city.Population AS Poblacion_Capital
FROM 
    country
JOIN 
    city ON city.ID = country.Capital;
        
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
