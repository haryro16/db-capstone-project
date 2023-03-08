
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='root', database='little_lemon_db')
cursor = db.cursor()

# Execute SQL statements
cursor.execute("show tables")

# Fetch results
results = cursor.fetchall()
for row in results:
    print(row)
# GetMaxQuantity()
GetMaxQuantitypr =   """
    CREATE PROCEDURE GetMaxQuantity()
    BEGIN
    SELECT MAX(b.quantity) AS max_quantity
    FROM bookings b
    INNER JOIN orders o ON b.orderId = o.orderId
    INNER JOIN customers c ON o.customerId = c.customerId
    INNER JOIN employees e ON o.employeeId = e.employeeId;
    END;
    """
#ManageBooking()

#UpdateBooking()
UpdateBooking = """
CREATE PROCEDURE UpdateBooking (
    IN p_booking_id INT,
    IN p_booking_date DATE
)
BEGIN
    UPDATE bookings
    SET booking_date = p_booking_date
    WHERE booking_id = p_booking_id;
END
"""
#AddBooking()
AddBookings ="""
CREATE PROCEDURE AddBooking (
    IN booking_id INT,
    IN customer_id INT,
    IN booking_date DATE,
    IN table_number INT
)
BEGIN
    INSERT INTO bookings (booking_id, customer_id, booking_date, table_number)
    VALUES (booking_id, customer_id, booking_date, table_number);
END
"""

#CancelBooking()
CancelBooking ="""
CREATE PROCEDURE CancelBooking (AddBooking
    IN p_booking_id INT
)
BEGIN
    DELETE FROM bookings
    WHERE booking_id = p_booking_id;
END
"""
CallCancelBooking = """CALL CancelBooking(1);"""