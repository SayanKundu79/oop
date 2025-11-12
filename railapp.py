import streamlit as st
import requests

# -------------------------------
# RAIL SYSTEM CLASS (OOP DESIGN)
# -------------------------------

class Rail:
    """
    A class to simulate Indian Rail Information system.
    """

    def __init__(self):
        self.api_key = "30c382602bfa67c8a7c580e6cfe2becb"  # Placeholder API key
        self.base_url = "http://indianrailapi.com/api/v2"
        self.train_no = None
        

    # Encapsulation - Setting and getting train number safely
    def set_train_number(self, train_no: str):
        if train_no.isdigit():
            self.train_no = train_no
        else:
            raise ValueError("Train number must be numeric")

    def get_train_number(self):
        return self.train_no

    # Abstraction - A method to fetch or simulate train schedule
    def get_train_schedule(self):
        """
        Normally fetches data from Indian Rail API,
        but currently uses simulated data for demonstration.
        """
        # Uncomment this part for real API call:
        # url = f"{self.base_url}/TrainSchedule/apikey/{self.api_key}/TrainNumber/{self.train_no}"
        # response = requests.get(url)
        # return response.json()

        # Simulated static data (for offline use)
        return [{
            "ResponseCode": "200",
            "Status": "SUCCESS",
            "Route": [
                {"SerialNo": "1", "StationCode": "DBG", "StationName": "DARBHANGA JN", "ArrivalTime": "08:35:00", "DepartureTime": "08:35:00", "Distance": "0"},
                {"SerialNo": "2", "StationCode": "SPJ", "StationName": "SAMASTIPUR J", "ArrivalTime": "09:25:00", "DepartureTime": "09:45:00", "Distance": "37"},
                {"SerialNo": "3", "StationCode": "MFP", "StationName": "MUZAFFARPUR", "ArrivalTime": "10:35:00", "DepartureTime": "10:40:00", "Distance": "89"},
                {"SerialNo": "4", "StationCode": "HJP", "StationName": "HAJIPUR JN.", "ArrivalTime": "11:25:00", "DepartureTime": "11:28:00", "Distance": "142"},
                {"SerialNo": "5", "StationCode": "SEE", "StationName": "SONPUR JN.", "ArrivalTime": "11:38:00", "DepartureTime": "11:40:00", "Distance": "148"},
                {"SerialNo": "6", "StationCode": "CPR", "StationName": "CHHAPRA JN.", "ArrivalTime": "12:45:00", "DepartureTime": "12:50:00", "Distance": "202"},
                {"SerialNo": "7", "StationCode": "SV", "StationName": "SIWAN JN.", "ArrivalTime": "13:40:00", "DepartureTime": "13:45:00", "Distance": "262"},
                {"SerialNo": "8", "StationCode": "GKP", "StationName": "GORAKHPUR JN", "ArrivalTime": "15:50:00", "DepartureTime": "16:05:00", "Distance": "380"},
                {"SerialNo": "9", "StationCode": "LKO", "StationName": "LUCKNOW JN.", "ArrivalTime": "20:55:00", "DepartureTime": "21:10:00", "Distance": "649"},
                {"SerialNo": "10", "StationCode": "CNB", "StationName": "KANPUR CENTR", "ArrivalTime": "22:48:00", "DepartureTime": "22:58:00", "Distance": "722"},
                {"SerialNo": "11", "StationCode": "NDLS", "StationName": "NEW DELHI", "ArrivalTime": "05:30:00", "DepartureTime": "05:30:00", "Distance": "1153"}
            ]
        }]

    # Polymorphism example (can be overridden later for Live or PNR)
    def display_result(self, data):
        """Display schedule neatly"""
        route = data[0]['Route']
        return route


# -------------------------------
# STREAMLIT WEB GUI
# -------------------------------

class RailGUI:
    """
    A Streamlit-based GUI for the Rail system.
    """

    def __init__(self):
        self.rail_system = Rail()

    def main_page(self):
        st.set_page_config(page_title="Indian Rail Info", page_icon="🚆", layout="centered")
        st.title("🚆 Indian Rail Information System")

        # Sidebar menu for different options
        option = st.sidebar.radio(
            "Choose an Option:",
            ("Check Live Train Status", "Check PNR Status", "Check Train Schedule")
        )

        if option == "Check Live Train Status":
            st.info("🔧 Live train status feature not implemented yet.")

        elif option == "Check PNR Status":
            st.info("🔧 PNR status feature not implemented yet.")

        elif option == "Check Train Schedule":
            self.train_schedule_ui()

    def train_schedule_ui(self):
        """Train schedule GUI section"""
        train_no = st.text_input("Enter Train Number:")
        if st.button("Get Train Schedule"):
            try:
                self.rail_system.set_train_number(train_no)
                data = self.rail_system.get_train_schedule()
                route = self.rail_system.display_result(data)

                st.success(f"✅ Showing Schedule for Train Number: {train_no}")
                st.write("---")
                st.table(route)

                st.subheader("Detailed Route Information")
                for station in route:
                    st.write(
                        f"**{station['SerialNo']}. {station['StationName']} ({station['StationCode']})**  \n"
                        f"🕒 Arrival: {station['ArrivalTime']} | 🕕 Departure: {station['DepartureTime']} | 🛣 Distance: {station['Distance']} km"
                    )

            except ValueError as e:
                st.error(str(e))


# -------------------------------
# MAIN ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    gui = RailGUI()
    gui.main_page()
