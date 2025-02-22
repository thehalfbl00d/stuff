# Team 24

# Taaxy

A modern tax management system built with PHP.

## Requirements

- PHP 8.1 or higher
- MySQL 5.7 or higher
- Composer
- Apache/Nginx web server

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thehalfbl00d/taxbrew.git
cd taxbrew
```

2. Install dependencies:
```bash
composer install
```

3. Configure your environment:
- Copy `.env.example` to `.env`
- Update database credentials in `.env`

4. Set up the database:
```bash
php scripts/setup-database.php
```

5. Start the development server:
```bash
php -S localhost:8000 -t public
```

## Project Structure

```
taxbrew/
├── app/               # Application source code
├── config/           # Configuration files
├── public/           # Web server root directory
├── storage/          # Logs and uploads
├── tests/            # Test suites
└── vendor/           # Composer dependencies
```

## Development

- Follow PSR-12 coding standards
- Write tests for new features
- Keep documentation up to date

## Testing

Run the test suite:
```bash
composer test
```

## License

This project is licensed under the MIT License.

