import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-password-recovery',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="recovery-container">
      <div class="recovery-card">
        <h2>Password Recovery</h2>
        <p>Enter your email address to receive a password reset link.</p>
        <form class="recovery-form">
          <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" placeholder="your.email@example.com" required>
          </div>
          <button type="submit" class="recovery-button">Send Reset Link</button>
        </form>
        <div class="back-to-login">
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

    .recovery-container {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      padding: 20px;
      box-sizing: border-box;
    }

    .recovery-card {
      background-color: #ffffff;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
      text-align: center;
      width: 100%;
      max-width: 400px;
    }

    h2 {
      color: #333;
      margin-bottom: 15px;
      font-size: 26px;
    }

    p {
      color: #666;
      margin-bottom: 30px;
      font-size: 16px;
      line-height: 1.5;
    }

    .recovery-form {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .form-group {
      text-align: left;
    }

    label {
      display: block;
      margin-bottom: 8px;
      color: #555;
      font-size: 14px;
      font-weight: bold;
    }

    input[type="email"] {
      width: calc(100% - 20px);
      padding: 12px 10px;
      border: 1px solid #ddd;
      border-radius: 8px;
      font-size: 16px;
      color: #333;
      transition: border-color 0.3s ease;
    }

    input[type="email"]:focus {
      border-color: #007bff;
      outline: none;
      box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
    }

    .recovery-button {
      background-color: #007bff;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 8px;
      font-size: 18px;
      cursor: pointer;
      transition: background-color 0.3s ease;
      margin-top: 10px;
    }

    .recovery-button:hover {
      background-color: #0056b3;
    }

    .back-to-login {
      margin-top: 30px;
      font-size: 15px;
    }

    .back-to-login a {
      color: #007bff;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .back-to-login a:hover {
      color: #0056b3;
      text-decoration: underline;
    }
  `]
})
export class PasswordRecoveryPageComponent {

}