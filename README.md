# Django Encyclopedia Project

## Overview

This Django project is an encyclopedia application that allows users to create, edit, and search for encyclopedia entries. The project also includes features such as random page navigation and Markdown to HTML conversion.

## Features

### Entry Page

- Visiting `/wiki/TITLE`, where TITLE is the title of an encyclopedia entry, renders a page displaying the contents of that entry.
- The view retrieves the content of the encyclopedia entry by calling the appropriate util function.
- If the requested entry does not exist, the user is presented with an error page indicating that the requested page was not found.
- If the entry exists, the user sees a page displaying the content of the entry. The page's title includes the name of the entry.

### Index Page

- The `index.html` page allows users to click on any entry name to be taken directly to that entry page.

### Search

- Users can type a query into the search box in the sidebar to search for an encyclopedia entry.
- If the query matches an entry name, the user is redirected to that entry's page.
- If the query does not match an entry name, the user is taken to a search results page displaying a list of entries with the query as a substring.
- Clicking on any entry name on the search results page takes the user to that entry's page.

### New Page

- Clicking "Create New Page" in the sidebar takes the user to a page where they can create a new encyclopedia entry.
- Users can enter a title and use a textarea to input Markdown content for the page.
- Clicking a button saves the new page.
- If an entry already exists with the provided title, the user is presented with an error message.
- Otherwise, the new entry is saved to disk, and the user is taken to the new entry's page.

### Edit Page

- On each entry page, users can click a link to be taken to a page where they can edit the entry's Markdown content in a textarea.
- The textarea is pre-populated with the existing Markdown content.
- Clicking a button saves the changes made to the entry.
- After saving, the user is redirected back to the entry's page.

### Random Page

- Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

- On each entry's page, any Markdown content in the entry file is converted to HTML using the python-markdown2 package before being displayed to the user. Install the package via `pip3 install markdown2`.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Kolade-dotcom/django-encyclopedia-project.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Visit [http://localhost:8000](http://localhost:8000) to access the application.

## Contributing

Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
