import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class AuthProvider with ChangeNotifier {
  final _storage = FlutterSecureStorage();
  String? _token;

  String? get token => _token;

  Future<void> login(String username, String password) async {
    // Simulasi login
    // Di sini kamu bisa menambahkan logika autentikasi sebenarnya
    _token = 'dummy_token';
    await _storage.write(key: 'token', value: _token);
    notifyListeners();
  }

  Future<void> logout() async {
    _token = null;
    await _storage.delete(key: 'token');
    notifyListeners();
  }
}

