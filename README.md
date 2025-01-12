# Rocket Upload

Rocket Upload is a powerful and intuitive file upload service designed for handling large files seamlessly. The project leverages modern technologies to provide a smooth user experience and robust backend support.

## Features

- Drag-and-drop file upload
- Large file support
- Real-time progress tracking
- Secure file handling and storage

## Technologies Used

- **Backend:** Python, flask
- **Frontend:** ReactJS
- **Styling:** Tailwind CSS
- **File Storage:** AWS S3

## Prerequisites

To set up and run the project locally, ensure you have the following:

- Python 3.11
- AWS account with an S3 bucket configured

## Installation

### 1. Clone the Repository

```bash
$ git clone https://github.com/minhchef/rocket-upload.git
$ cd rocket-upload
```

### 2. Install Dependencies

Navigate to the `backend` and `frontend` directories to install dependencies:

#### Backend
```bash
$ pip install requirements.txt
```

#### Frontend
```bash
$ cd ../src
$ pnpm install
```

### 3. Configure Environment Variables

#### Backend

Create a `.env` file in the `backend` directory with the following content:

```
PORT=5000
MONGO_URI=your_mongo_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_BUCKET_NAME=your_s3_bucket_name
```

#### Frontend

Create a `.env` file in the `frontend` directory with the following content:

```
REACT_APP_API_BASE_URL=http://localhost:5000
```

### 4. Run the Project
- docker-composer up -d
- access the site by port localhost:3000
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to reach out via the [issues](https://github.com/minhchef/rocket-upload/issues) section for questions or feedback!

