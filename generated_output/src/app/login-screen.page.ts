import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login-screen',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    FormsModule
  ],
  template: `
    <div class="login-container">
      <h2>Login</h2>
      <form (ngSubmit)="login()">
        <div class="form-group">
          <label for="username">Username or Email:</label>
          <input type="text" id="username" name="username" [(ngModel)]="username" required aria-label="Username or Email">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" name="password" [(ngModel)]="password" required aria-label="Password">
        </div>
        <button type="submit" class="login-button">Log In</button>
      </form>
      <div class="forgot-password">
        <a routerLink="/forgot-password-screen">Forgot Password?</a>
      </div>
    </div>
  `,
  styles: [`
    :host {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      background-color: #f8f9fa; /* Light neutral background */
      font-family: Arial, sans-serif;
    }

    .login-container {
      background-color: #ffffff;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
      text-align: center;
    }

    h2 {
      color: #333;
      margin-bottom: 30px;
      font-size: 1.8em;
      font-weight: 600;
    }

    .form-group {
      margin-bottom: 20px;
      text-align: left;
    }

    label {
      display: block;
      margin-bottom: 8px;
      color: #555;
      font-size: 0.95em;
      font-weight: 500;
    }

    input[type="text"],
    input[type="password"] {
      width: calc(100% - 24px); /* Account for padding */
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 8px;
      font-size: 1em;
      color: #333;
      transition: border-color 0.2s ease-in-out;
    }

    input[type="text"]:focus,
    input[type="password"]:focus {
      border-color: #007bff; /* Primary blue for focus */
      outline: none;
      box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.2);
    }

    .login-button {
      width: 100%;
      padding: 14px;
      background-color: #007bff; /* Primary blue */
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 1.1em;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.2s ease-in-out, transform 0.1s ease-in-out;
      margin-top: 20px;
    }

    .login-button:hover {
      background-color: #0056b3; /* Slightly darker blue on hover */
      transform: translateY(-1px);
    }

    .login-button:active {
      transform: translateY(0);
    }

    .forgot-password {
      margin-top: 25px;
      font-size: 0.9em;
    }

    .forgot-password a {
      color: #007bff; /* Primary blue */
      text-decoration: none;
      transition: color 0.2s ease-in-out;
    }

    .forgot-password a:hover {
      color: #0056b3; /* Slightly darker blue on hover */
      text-decoration: underline;
    }
  `]
})
export class LoginScreenPageComponent {
  username: string = '';
  password: string = '';

  constructor() { }

  login(): void {
    // Placeholder for login logic
    console.log('Login attempt with:', this.username, this.password);
    alert('Login functionality not implemented yet!');
  }
}