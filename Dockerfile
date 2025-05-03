FROM node:18

# Set the working directory
WORKDIR /app

# Copy the contents of your project into the container
COPY . .

# Install dependencies
RUN npm install

# Set the environment variable to handle OpenSSL issues in Node.js v17 and above
ENV NODE_OPTIONS=--openssl-legacy-provider

# Run the app
CMD ["npm", "start"]
