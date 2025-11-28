import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-password-reset',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="password-reset-container">
      <div class="card">
        <h1>Password Reset</h1>
        <p>Enter your email address to receive a password reset link.</p>
        <form class="password-reset-form">
          <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" placeholder="your.email&#64;example.com" required>
          </div>
          <button type="submit" class="reset-button">Send Reset Link</button>
        </form>
        <div class="back-to-login">
          Remembered your password? &lt;a routerLink="/login-screen"&gt;Back to Login&lt;/a&gt;
        </div>
      </div>
    </div>
  `,
  styles: [`
    :host {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background-color: #f8f8f8;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .password-reset-container {
      width: 100%;
      max-width: 400px;
      padding: 20px;
    }

    .card {
      background-color: #ffffff;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      text-align: center;
    }

    h1 {
      color: #333;
      margin-bottom: 20px;
      font-size: 28px;
      font-weight: 600;
    }

    p {
      color: #666;
      margin-bottom: 25px;
      line-height: 1.6;
    }

    .form-group {
      margin-bottom: 20px;
      text-align: left;
    }

    label {
      display: block;
      margin-bottom: 8px;
      color: #555;
      font-weight: 500;
      font-size: 14px;
    }

    input[type="email"] {
      width: calc(100% - 20px);
      padding: 12px 10px;
      border: 1px solid #ddd;
      border-radius: 6px;
      font-size: 16px;
      color: #333;
      transition: border-color 0.2s ease-in-out;
    }

    input[type="email"]:focus {
      outline: none;
      border-color: #007bff;
      box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
    }

    .reset-button {
      width: 100%;
      padding: 12px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 18px;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.2s ease-in-out;
      margin-top: 15px;
    }

    .reset-button:hover {
      background-color: #0056b3;
    }

    .back-to-login {
      margin-top: 25px;
      font-size: 14px;
      color: #777;
    }

    .back-to-login a {
      color: #007bff;
      text-decoration: none;
      font-weight: 500;
    }

    .back-to-login a:hover {
      text-decoration: underline;
    }
  `]
})
export class PasswordResetPageComponent {}