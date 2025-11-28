import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-forgot-password',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="container">
      <div class="card">
        <h2>Forgot Password&#63;</h2>
        <p>Enter your email address and we'll send you a link to reset your password.</p>
        <form (ngSubmit)="onSubmit()">
          <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required aria-label="Email Address">
          </div>
          <button type="submit" class="submit-button">Reset Password</button>
        </form>
        <div class="back-link">
          <a routerLink="/login-screen">Back to Login</a>
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
      background-color: #f0f2f5;
      font-family: Arial, sans-serif;
    }
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
    }
    .card {
      background-color: #ffffff;
      padding: 2.5rem;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
      text-align: center;
    }
    h2 {
      color: #333333;
      margin-bottom: 1rem;
      font-size: 1.8em;
    }
    p {
      color: #666666;
      margin-bottom: 1.5rem;
      font-size: 1em;
      line-height: 1.5;
    }
    .form-group {
      margin-bottom: 1.5rem;
      text-align: left;
    }
    label {
      display: block;
      margin-bottom: 0.5rem;
      color: #555555;
      font-size: 0.9em;
      font-weight: bold;
    }
    input[type="email"] {
      width: calc(100% - 20px);
      padding: 12px 10px;
      border: 1px solid #cccccc;
      border-radius: 8px;
      font-size: 1em;
      box-sizing: border-box;
    }
    input[type="email"]:focus {
      outline: none;
      border-color: #007bff;
      box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
    }
    .submit-button {
      width: 100%;
      padding: 12px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 1.1em;
      cursor: pointer;
      transition: background-color 0.2s ease;
      margin-top: 1rem;
    }
    .submit-button:hover {
      background-color: #0056b3;
    }
    .back-link {
      margin-top: 1.5rem;
      font-size: 0.9em;
    }
    .back-link a {
      color: #007bff;
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .back-link a:hover {
      text-decoration: underline;
      color: #0056b3;
    }
  `]
})
export class ForgotPasswordPageComponent {
  constructor() { }

  onSubmit() {
    // Logic to handle password reset request
    console.log('Password reset requested');
  }
}