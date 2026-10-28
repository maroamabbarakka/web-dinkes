// Firebase Web SDK Modular Setup
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { 
  getFirestore, 
  collection, 
  getDocs, 
  getDoc, 
  doc, 
  query, 
  orderBy, 
  limit, 
  where 
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

// Konfigurasi resmi Firebase Dinas Kesehatan Kabupaten Pinrang
export const firebaseConfig = {
  apiKey: "AIzaSyDK7sOlRHmc8WyJZsxQP032NYHtG9vcn-U",
  authDomain: "dinkes-pinrang.firebaseapp.com",
  projectId: "dinkes-pinrang",
  storageBucket: "dinkes-pinrang.firebasestorage.app",
  messagingSenderId: "281517642678",
  appId: "1:281517642678:web:a8b20c74bc8302fba5e717"
};

// Inisialisasi Firebase App
export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export { collection, getDocs, getDoc, doc, query, orderBy, limit, where };
