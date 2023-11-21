# USForest Service App FRONTEND

## Introduction

This frontend is part of the USForest Service App, designed to provide users with comprehensive data regarding forest inventory across the United States through the easy access of the `BigQuery` cloud data with an easy to use *Query Builder*.

## Technologies Used

- **Next.js**: A React framework that provides server-side rendering and generates static websites for lightning-fast page loads and SEO-friendly content.
- **React**: A JavaScript library for building user interfaces, known for its declarative and component-based approach.
- **TypeScript**: A strongly typed programming language that builds on JavaScript, giving you better tooling at any scale.
- **Tailwind CSS**: A utility-first CSS framework for rapidly building custom designs.
- **Jest**: A delightful JavaScript Testing Framework with a focus on simplicity.
- **Testing Library**: React Testing Library to test the project in a way that's closer to how users interact with the app.
- **Docker**: Utilized for containerizing the application, ensuring consistency across various development and deployment environments.
- **GitHub Actions**: For continuous integration and continuous deployment (CI/CD), automating the testing and deployment process.

## Design Decisions

- **Framework Choice**: Next.js was chosen for its hybrid static & server rendering, TypeScript support, smart bundling, route pre-fetching, and more. This allows us to achieve high performance and enhance the user experience with fast page loads.
- **Component Architecture**: A component-based architecture was adopted to create reusable and isolated pieces of UI, which can be independently developed and tested.
- **Styling**: Tailwind CSS was selected for its ability to write custom styles without leaving HTML, leading to faster development cycles and more maintainable code.
- **Testing**: Jest and React Testing Library are the industry standards for testing React applications. They provide a powerful and flexible testing environment with a focus on simplicity.
- **Containerization**: Docker is used to encapsulate the application environment, which streamlines development and eliminates the "it works on my machine" problem.
- **CI/CD**: GitHub Actions automate our workflows, making the process of integrating changes and deploying them to production seamless and error-free.

## Getting Started

To run the project locally, make sure you have Node.js and npm installed. Clone the repository and navigate to the `frontend/next-pages` directory:



Install dependencies:

```bash
npm install
```

Run the development server if you wish to work directly on the code (no docker):
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result. (If you launch from the docker, the port will be  [http://localhost:9000](http://localhost:9000) )

## Testing

To run tests and generate coverage reports locally:

```bash
npm run test -- --coverage
```

**NOTE**: Our *Github Actions CI/CD workflow* run this automatically.

## Deployment

The app is containerized using Docker, allowing for easy deployment to any services that support containerized applications.

## Contributing

This app is a proof of concept, its not being actively developed or maintained, do look for other projects!

## License

This project doesnt have a license attached.

<br>

---