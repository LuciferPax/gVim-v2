# plugins/auto_close.py

def run(api):
    def auto_close(event):
        char = event.char
        if char in "([{\'\"":
            matching_char = {'(': ')', '[': ']', '{': '}', "'": "'", '"': '"'}[char]
            cursor_pos = api.get_cursor_position()

            # Insert both the opening and closing characters
            api.insert_text(cursor_pos, char + matching_char)

            # Set cursor position between the pair
            api.set_cursor_position(f"{cursor_pos}+1c")

            # Stop further event propagation to avoid duplication
            return "break"

    # Bind the auto-close function to the typing events
    api.bind_key("(", auto_close)
    api.bind_key("[", auto_close)
    api.bind_key("{", auto_close)
    api.bind_key("'", auto_close)
    api.bind_key('"', auto_close)
