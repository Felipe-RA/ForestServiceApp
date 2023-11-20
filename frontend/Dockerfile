FROM node:20 
# 20 is the latest LTS version of node as of 18/11/2023.  https://endoflife.date/nodejs

# Set the working directory to /app/next-pages
WORKDIR /app/next-pages

# Copy the package.json (and package-lock.json) to /app/next-pages
COPY next-pages/package*.json ./

RUN npm install

# Copy the rest of the Next.js files into the working directory
COPY next-pages/ ./

# Build the Next.js application
RUN npm run build

# Command to start the app
CMD ["npm", "start"]
