import pyodbc

def get_connection():
    """
    Establishes a connection to the database.
    Adjust the connection string as per your database configuration.
    """
    return pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=ANJANA;"
        "Database=Virtual_Healthcare;"
        "Trusted_Connection=yes;"
    )

def fetch_events():
    """
    Retrieves all event records from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spRetrieveEvents")
        events = cursor.fetchall()
    return events

def add_event(organizer_id, venue_id, category_id, title, description, start_date, end_date, event_status):
    """
    Adds a new event record to the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spInsertEvent ?, ?, ?, ?, ?, ?, ?, ?",
                       (organizer_id, venue_id, category_id, title, description, start_date, end_date, event_status))
        conn.commit()

def update_event(event_id, organizer_id, venue_id, category_id, title, description, start_date, end_date, event_status):
    """
    Updates an existing event record in the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spUpdateEvent ?, ?, ?, ?, ?, ?, ?, ?, ?",
                       (event_id, organizer_id, venue_id, category_id, title, description, start_date, end_date, event_status))
        conn.commit()

def delete_event(event_id):
    """
    Deletes an event record from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spDeleteEvent ?", (event_id,))
        conn.commit()

def fetch_registrations():
    """
    Retrieves all registration records from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spRetrieveRegistration")
        registrations = cursor.fetchall()
        
    # Convert date objects to strings with the format "YYYY-MM-DD"
    formatted_registrations = []
    for registration in registrations:
        formatted_registration = list(registration)  # Convert to list to modify
        formatted_registration[3] = registration[3].strftime("%Y-%m-%d")  # Format the date
        formatted_registrations.append(formatted_registration)
        
    return formatted_registrations


def add_registration(event_id, attendee_id, registration_date, payment_status, price, discount, ticket_type):
    """
    Adds a new registration record to the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spInsertRegistration ?, ?, ?, ?, ?, ?, ?", 
                       (event_id, attendee_id, registration_date, payment_status, price, discount, ticket_type))
        conn.commit()



def add_organizer(name, description, address, contact_email, contact_phone):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spInsertOrganizer ?, ?, ?, ?, ?",
                       (name, description, address, contact_email, contact_phone))
        conn.commit()

def fetch_organizers():
    """
    Retrieves all organizer records from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spRetrieveOrganizer")
        organizers = cursor.fetchall()
        
    # Convert date objects to strings with the format "YYYY-MM-DD"
    formatted_organizers = []
    for organizer in organizers:
        formatted_organizer = list(organizer)  # Convert to list to modify
        # Format any date fields here if needed
        formatted_organizers.append(formatted_organizer)
        
    return formatted_organizers


def update_organizer(organizer_id, name, description, address, contact_email, contact_phone):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spUpdateOrganizer ?, ?, ?, ?, ?, ?",
                       (organizer_id, name, description, address, contact_email, contact_phone))
        conn.commit()

def delete_organizer(organizer_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spDeleteOrganizer ?", (organizer_id,))
        conn.commit()

def fetch_venues():
    """
    Retrieves all venue records from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spRetrieveVenue")
        venues = cursor.fetchall()
        
    # Convert any fields here if needed
    formatted_venues = []
    for venue in venues:
        formatted_venue = list(venue)  # Convert to list to modify
        # Format any fields here if needed
        formatted_venues.append(formatted_venue)
        
    return formatted_venues


def add_venue(name, address, city, state, capacity, amenities):
    """
    Adds a new venue record to the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spInsertVenue ?, ?, ?, ?, ?, ?", (name, address, city, state, capacity, amenities))
        conn.commit()

def update_venue(venue_id, name, address, city, state, capacity, amenities):
    """
    Updates an existing venue record in the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spUpdateVenue ?, ?, ?, ?, ?, ?, ?", (venue_id, name, address, city, state, capacity, amenities))
        conn.commit()

def delete_venue(venue_id):
    """
    Deletes a venue record from the database.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("EXEC spDeleteVenue ?", (venue_id,))
        conn.commit()

def fetch_event_summary():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Event_Summary")
        events = cursor.fetchall()

    formatted_events = []
    for event in events:
        formatted_event = list(event)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_events.append(formatted_event)

    return formatted_events

def fetch_sponsor_contribution_summary():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sponsor_Contribution_Summary")
        contributions = cursor.fetchall()

    formatted_contributions = []
    for contribution in contributions:
        formatted_contribution = list(contribution)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_contributions.append(formatted_contribution)

    return formatted_contributions

def fetch_attendee_registration_summary():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Attendee_Registration_Summary")
        registrations = cursor.fetchall()

    formatted_registrations = []
    for registration in registrations:
        formatted_registration = list(registration)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_registrations.append(formatted_registration)

    return formatted_registrations

def fetch_event_feedback_analysis():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Event_Feedback_Analysis")
        feedbacks = cursor.fetchall()

    formatted_feedbacks = []
    for feedback in feedbacks:
        formatted_feedback = list(feedback)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_feedbacks.append(formatted_feedback)

    return formatted_feedbacks

def fetch_ticket_sales_analysis():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ticket_Sales_Analysis")
        ticket_sales = cursor.fetchall()

    formatted_ticket_sales = []
    for ticket_sale in ticket_sales:
        formatted_ticket_sale = list(ticket_sale)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_ticket_sales.append(formatted_ticket_sale)

    return formatted_ticket_sales

def fetch_speaker_engagement():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Speaker_Engagement")
        engagements = cursor.fetchall()

    formatted_engagements = []
    for engagement in engagements:
        formatted_engagement = list(engagement)  # Convert to list to modify if needed
        # Format any fields here if needed
        formatted_engagements.append(formatted_engagement)

    return formatted_engagements