# SeleniumRouteCrawler

SeleniumRouteCrawler is a Python tool designed for efficiently fetching API routes and their corresponding titles concurrently. This tool is built with the goal of providing a quick and parallelized approach to exploring and collecting information about API endpoints.

## Features

- **Concurrency:** Utilizes multiprocessing to fetch API routes concurrently, taking advantage of multi-core processors.
- **Headless Mode:** Employs Selenium in headless mode for efficient web page interaction during route fetching.
- **Customizable Range:** Allows users to specify the start and end range of API routes to fetch, providing flexibility in exploration.
- **Append to Existing Data:** Appends new results to an existing JSON file if it already exists, enabling cumulative data collection.

## Prerequisites

Ensure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [Chrome browser](https://www.google.com/chrome/) installed (for Selenium interaction)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/floki1250/SeleniumRouteCrawler.git
   cd SeleniumRouteCrawler
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using the following command, replacing `<base_url>`, `<start_range>`, and `<end_range>` with your desired values:

```bash
python SeleniumRouteCrawler.py <base_url> <start_range> <end_range>
```

Example:

```bash
python SeleniumRouteCrawler.py https://test.net/d/ 1 1000
```

## Output

The tool will append the fetched data to a file named `api_routes.json` in the current directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace placeholder values such as `<base_url>`, `<start_range>`, `<end_range>`, and `https://github.com/yourusername/RouteFetcher.git` with the actual values and information specific to your tool and repository.
