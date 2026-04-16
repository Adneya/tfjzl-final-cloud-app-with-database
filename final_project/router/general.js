const express = require('express');
let books = require("./booksdb.js");
let isValid = require("./auth_users.js").isValid;
let users = require("./auth_users.js").users;
const public_users = express.Router();
const axios = require('axios');

const BASE_URL = 'http://localhost:5000';

const findBooksBy = (predicate) => {
  const filteredBooks = {};

  Object.entries(books).forEach(([isbn, book]) => {
    if (predicate(book)) {
      filteredBooks[isbn] = book;
    }
  });

  return filteredBooks;
};


public_users.post("/register", (req,res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ message: 'Username and password are required' });
  }

  if (!isValid(username)) {
    return res.status(409).json({ message: 'User already exists' });
  }

  users.push({ username, password });
  return res.status(200).json({ message: 'User successfully registered. Now you can login' });
});

// Get the book list available in the shop
public_users.get('/',function (req, res) {
  return res.status(200).json(books);
});

// Get book details based on ISBN
public_users.get('/isbn/:isbn',function (req, res) {
  const { isbn } = req.params;
  const book = books[isbn];

  if (!book) {
    return res.status(404).json({ message: 'Book not found' });
  }

  return res.status(200).json(book);
 });
  
// Get book details based on author
public_users.get('/author/:author',function (req, res) {
  const authorParam = decodeURIComponent(req.params.author).toLowerCase();
  const filteredBooks = findBooksBy((book) => book.author.toLowerCase() === authorParam);

  if (Object.keys(filteredBooks).length === 0) {
    return res.status(404).json({ message: 'No books found for the given author' });
  }

  return res.status(200).json(filteredBooks);
});

// Get all books based on title
public_users.get('/title/:title',function (req, res) {
  const titleParam = decodeURIComponent(req.params.title).toLowerCase();
  const filteredBooks = findBooksBy((book) => book.title.toLowerCase() === titleParam);

  if (Object.keys(filteredBooks).length === 0) {
    return res.status(404).json({ message: 'No books found for the given title' });
  }

  return res.status(200).json(filteredBooks);
});

//  Get book review
public_users.get('/review/:isbn',function (req, res) {
  const { isbn } = req.params;
  const book = books[isbn];

  if (!book) {
    return res.status(404).json({ message: 'Book not found' });
  }

  return res.status(200).json(book.reviews);
});

// Axios implementation using promise callbacks
public_users.get('/promise/books', function (req, res) {
  axios
    .get(`${BASE_URL}/`)
    .then((response) => res.status(200).json(response.data))
    .catch((error) => {
      return res.status(500).json({
        message: 'Unable to fetch books using promise callback',
        error: error.message
      });
    });
});

public_users.get('/promise/isbn/:isbn', function (req, res) {
  const { isbn } = req.params;

  axios
    .get(`${BASE_URL}/isbn/${encodeURIComponent(isbn)}`)
    .then((response) => res.status(200).json(response.data))
    .catch((error) => {
      const statusCode = error.response?.status || 500;

      return res.status(statusCode).json({
        message: 'Unable to fetch book by ISBN using promise callback',
        error: error.response?.data || error.message
      });
    });
});

// Axios implementation using async/await
public_users.get('/async/author/:author', async function (req, res) {
  const { author } = req.params;

  try {
    const response = await axios.get(`${BASE_URL}/author/${encodeURIComponent(author)}`);
    return res.status(200).json(response.data);
  } catch (error) {
    const statusCode = error.response?.status || 500;

    return res.status(statusCode).json({
      message: 'Unable to fetch books by author using async/await',
      error: error.response?.data || error.message
    });
  }
});

public_users.get('/async/title/:title', async function (req, res) {
  const { title } = req.params;

  try {
    const response = await axios.get(`${BASE_URL}/title/${encodeURIComponent(title)}`);
    return res.status(200).json(response.data);
  } catch (error) {
    const statusCode = error.response?.status || 500;

    return res.status(statusCode).json({
      message: 'Unable to fetch books by title using async/await',
      error: error.response?.data || error.message
    });
  }
});

module.exports.general = public_users;
