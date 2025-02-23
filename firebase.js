// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAu8qsmHHPJxyGPyqHCJkCvBSkP1GcgBoE",
  authDomain: "project-7ceee.firebaseapp.com",
  projectId: "project-7ceee",
  storageBucket: "project-7ceee.firebasestorage.app",
  messagingSenderId: "951091829559",
  appId: "1:951091829559:web:f0b432ee5e9668a3e798b2",
  measurementId: "G-WNLRJ7KJWM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);