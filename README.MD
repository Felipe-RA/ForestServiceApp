# US Forest Service Inventory Query Builder

This project serves as a query interface to the US Forest Service public dataset hosted on Google Cloud. It is designed as a monorepo containing both the frontend and backend code, utilizing CI/CD with GitHub Actions for automation, and integrating SonarCloud for code quality assurance.

The public data from the US Forest Service is  available openly and freely for non commercial purposes at [Google Cloud](https://console.cloud.google.com/marketplace/product/us-forest-service/forest-inventory-analysis).

## Table of Contents

- [Prerequisites](#prerequisites)
- [CI/CD and Quality Assurance](#ci-cd-and-quality-assurance)
- [Connecting to Google Cloud BigQuery](#connecting-to-google-cloud-bigquery)
- [Project Planning](#project-planning)
- [Known Improvements](#known-improvements-to-implement)

## PROJECT PLANNING

A Backlog was defined through the usage of **Github Projects**. Right now its public and viewable by everyone:

- [Github Project: Project Direction](https://github.com/users/Felipe-RA/projects/2)

---

## CI/CD Compatibility and SonarCloud for **Software Quality Assurance**

This project is compatible with Github Actions + Sonacloud Analysis, and its configured as a **MONOREPO** that analyzes the `frontend` and the `backend` on two different processes!

![SonarCloud GitHub Action check](images/sonarcloud-action.png)

## Prerequisites

To run this project locally, you need to provide a `google_cloud_keyfile_service_account.json` at the root of your project directory. This file is essential for authenticating with Google Cloud BigQuery and must contain credentials for a service account with the following roles:

- BigQuery Data Viewer
- BigQuery Job User
- BigQuery Metadata Viewer

Please ensure that you have the appropriate permissions and roles assigned to your service account before proceeding.

The file should look like this (this is a placeholder):

```json
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
  "universe_domain": ""
}
```

## CI/CD and Quality Assurance

Our CI/CD pipeline is built with GitHub Actions, enabling automated unit testing and code coverage generation on every push and pull request. We've integrated SonarCloud to perform thorough code quality checks, ensuring that code health is maintained throughout the development lifecycle.

!!! SonarCloud Quality Gate Passed image goes here. Describe it as a badge indicating the successful quality check. !!!

## Connecting to Google Cloud BigQuery

We've established a connection to Google Cloud BigQuery by leveraging a service account. The credentials for this account are securely managed and used to authenticate API requests, allowing our backend to interact with BigQuery datasets.

## Project Planning

Project management and task tracking are handled using **GitHub Projects**. Our project board is publicly available and provides insight into our development process:

- [GitHub Project: Project Direction](https://github.com/users/Felipe-RA/projects/2)

## Known Improvements to Implement

While we've made significant progress, there's always room for improvement. Here are some enhancements we're considering:

- **Federated Permissions**: Transitioning from using a key file to federated permissions for the Google Cloud service account would enhance security.
- **Integration Testing**: Implementing integration tests would ensure our components work together seamlessly.
- **Frontend Business Functionality**: Due to time constraints and my commitment to completing and defending my Machine Learning research, some frontend features and tests are pending development.

Preprint of my Machine Learning research available: [UdeAI Forest Research Preprint](https://github.com/Felipe-RA/udeai_forest/blob/main/preprint.pdf)

---

We are excited about the potential of this project and look forward to continual improvement and collaboration.
