import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import load_ratings, add_rating, delete_rating
from analysis import get_summary
from charts import show_rating_chart, show_genre_chart

class SongRatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("P69 - Song Rating & Audience Preference Analysis")
        self.root.geometry("1050x650")
        self.root.minsize(950, 600)

        title = tk.Label(root, text="Song Rating & Audience Preference Analysis",
                         font=("Arial", 20, "bold"))
        title.pack(pady=12)

        form = ttk.LabelFrame(root, text="Add Song Rating", padding=12)
        form.pack(fill="x", padx=15, pady=5)

        labels = ["Member Name", "Song", "Artist", "Genre", "Playlist", "Rating (1-5)"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=0, column=i, padx=5, pady=4)
            entry = ttk.Entry(form, width=18)
            entry.grid(row=1, column=i, padx=5, pady=4)
            self.entries[label] = entry

        ttk.Button(form, text="Add Rating", command=self.add_record).grid(
            row=1, column=6, padx=10
        )
        ttk.Button(form, text="Clear", command=self.clear_form).grid(
            row=1, column=7, padx=5
        )

        table_frame = ttk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("ID", "Member", "Song", "Artist", "Genre", "Playlist", "Rating")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        widths = [55, 130, 160, 130, 110, 130, 70]
        for col, width in zip(columns, widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        buttons = ttk.Frame(root)
        buttons.pack(pady=5)
        ttk.Button(buttons, text="Refresh", command=self.refresh).pack(side="left", padx=5)
        ttk.Button(buttons, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=5)
        ttk.Button(buttons, text="Show Summary", command=self.summary).pack(side="left", padx=5)
        ttk.Button(buttons, text="Song Rating Chart", command=show_rating_chart).pack(side="left", padx=5)
        ttk.Button(buttons, text="Genre Preference Chart", command=show_genre_chart).pack(side="left", padx=5)
        ttk.Button(buttons, text="Exit", command=root.destroy).pack(side="left", padx=5)

        self.status = tk.Label(root, text="", anchor="w")
        self.status.pack(fill="x", padx=15, pady=5)

        self.refresh()

    def add_record(self):
        values = [self.entries[x].get().strip() for x in self.entries]
        member, song, artist, genre, playlist, rating = values

        if not all(values):
            messagebox.showwarning("Missing Data", "Please fill all fields.")
            return

        try:
            rating = float(rating)
            if not 1 <= rating <= 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Rating", "Rating must be a number from 1 to 5.")
            return

        try:
            add_rating(member, song, artist, genre, playlist, rating)
            self.clear_form()
            self.refresh()
            messagebox.showinfo("Success", "Rating added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        df = load_ratings()
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=(
                row["ID"], row["Member"], row["Song"], row["Artist"],
                row["Genre"], row["Playlist"], row["Rating"]
            ))
        self.status.config(text=f"Total ratings: {len(df)}")

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Record", "Please select a record to delete.")
            return

        item = self.tree.item(selected[0])
        record_id = item["values"][0]

        if messagebox.askyesno("Confirm Delete", "Delete selected rating?"):
            delete_rating(record_id)
            self.refresh()

    def summary(self):
        summary = get_summary()
        messagebox.showinfo("Audience Preference Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = SongRatingApp(root)
    root.mainloop()
