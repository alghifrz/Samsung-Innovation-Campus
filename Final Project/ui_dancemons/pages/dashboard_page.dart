import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/auth_provider.dart';

class DashboardPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Dashboard'),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () async {
              await authProvider.logout();
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Selamat Datang!',
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 20),
            // Contoh tampilan tantangan
            ElevatedButton(
              onPressed: () {
                // Logika untuk mengakses dan menampilkan tantangan
              },
              child: Text('Lihat Tantangan'),
            ),
          ],
        ),
      ),
    );
  }
}
