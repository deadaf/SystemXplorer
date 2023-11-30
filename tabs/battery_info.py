from tkinter import Frame, Label, Tk
import psutil


def populate_battery_info_tab(battery_tab: Frame, root: Tk):
    def update():
        try:
            for widget in battery_tab.winfo_children():
                widget.destroy()

            # Get battery information
            battery = psutil.sensors_battery()

            if battery:
                charge_percent = battery.percent
                remaining_time = (
                    battery.secsleft // 60 if battery.power_plugged else None
                )
                battery_status = "Charging" if battery.power_plugged else "Discharging"
                battery_health = (
                    "Healthy"
                    if battery.percent > 80
                    else "Low"
                    if battery.percent > 20
                    else "Critical"
                )

                Label(
                    battery_tab,
                    text=f"Charge Level: {charge_percent}%",
                ).pack(pady=5)
                Label(
                    battery_tab,
                    text=f"Remaining Time: {remaining_time} minutes"
                    if remaining_time
                    else "Not Plugged In",
                ).pack()
                Label(battery_tab, text=f"Battery Status: {battery_status}").pack()
                Label(battery_tab, text=f"Battery Health: {battery_health}").pack()

            else:
                Label(
                    battery_tab,
                    text="Battery information not available",
                    fg="red",
                ).pack(pady=10)

        except Exception as e:
            # Handle errors, e.g., if battery information retrieval fails
            Label(battery_tab, text=f"Error: {e}", fg="red").pack(pady=10)

        root.after(1000, update)  # run itself again after 1000 ms

    update()
