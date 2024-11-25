VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   7410
   ClientLeft      =   110
   ClientTop       =   450
   ClientWidth     =   9100.001
   OleObjectBlob   =   "UserFormGraus.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub btnConverter_Click()
Dim C, F As Integer
C = Val(txtgraus.Value)
F = (1.8 * C) + 32
lblresultado.Caption = Str(F)
End Sub

Private Sub ToggleButton1_Click()
txtgraus.Value = " "
lblresultado.Caption = " "
End Sub
