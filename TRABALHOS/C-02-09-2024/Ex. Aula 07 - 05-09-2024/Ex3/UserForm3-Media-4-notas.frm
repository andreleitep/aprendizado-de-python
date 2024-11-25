VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm3 
   Caption         =   "UserForm2"
   ClientHeight    =   3765
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   6120
   OleObjectBlob   =   "UserForm3-Media-4-notas.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm3"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub CommandButton1_Click()

Dim N1, N2, N3, N4 As Double
Dim Media As Double

N1 = Val(txt1.Value)
N2 = Val(txt2.Value)
N3 = Val(txt3.Value)
N4 = Val(txt4.Value)

Media = (N1 + N2 + N3 + N4) / 4

lblMedia = "Média: " & Str(Media)

End Sub
