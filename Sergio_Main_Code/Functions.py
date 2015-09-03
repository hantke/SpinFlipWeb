################################################ Package ####################################################
import numpy as np
import Mate as M
import Database as D
################################################ Functions ##################################################

def Locate_Prog(a,b,Des_ID,Arr_Pro_N_ID):
	#print a,b,Des_ID,Arr_Pro_N_ID[(a+b)/2]
	if Arr_Pro_N_ID[a] == Des_ID:	return a
	if Arr_Pro_N_ID[b] == Des_ID:	return b
	
	m = (b+a)/2
	if Arr_Pro_N_ID[m] == Des_ID:	return m
	elif abs(a-b) < 2: return -99
	elif Arr_Pro_N_ID[m] > Des_ID:	return Locate_Prog(a,m,Des_ID,Arr_Pro_N_ID)
	else:	return  Locate_Prog(m,b,Des_ID,Arr_Pro_N_ID)

def Locate_MainProg(index,Des_ID,Arr_Pro_N_ID,Arr_Mass):
	i = index
	Max_Mass = Arr_Mass[index]
	Main_ID = index
	Next_Mass = -1
	Next_ID = -1
	Nprog = 1
	while i >= 0 and Arr_Pro_N_ID[i-1] == Des_ID:
		i -= 1
		Nprog += 1
		if Arr_Mass[i] > Max_Mass:
			Next_Mass = Max_Mass
			Next_ID = Main_ID
			Max_Mass = Arr_Mass[i]
			Main_ID = i
		elif Arr_Mass[i] > Next_Mass:
			Next_Mass = Arr_Mass[i]
			Next_ID = i
	i = index
	while i < len(Arr_Pro_N_ID)-1 and Arr_Pro_N_ID[i+1] == Des_ID:
		i += 1
		Nprog += 1
		if Arr_Mass[i] > Max_Mass:
			Next_Mass = Max_Mass
			Next_ID = Main_ID
			Max_Mass = Arr_Mass[i]
			Main_ID = i
		elif Arr_Mass[i] > Next_Mass:
			Next_Mass = Arr_Mass[i]
			Next_ID = i
	return int(Nprog),Main_ID,Max_Mass,Next_ID,Next_Mass
def Delta_M(M_prog,M_des):
	return abs(M_prog-M_des)/M_des


def F_2D_Histogram(D_ID,D_J,P_J,P2_J,D_Npart):
	Angle_1 = []
	Angle_2 = []
	Angle_3 = []
	Angle_4 = []
	for i in range(len(D_ID)):
		index = F.Locate_Prog(0,len(P_ID)-1,D_ID[i],P_New_ID)
		if index >= 0:	Nprog,Main_ID,Max_Mass,Next_ID,Next_Mass  = F.Locate_MainProg(index,D_ID[i],P_New_ID,P_Npart)
		else:	Nprog,Main_ID,Max_Mass  = -99,-99,-99
		index2 = F.Locate_Prog(0,len(P2_ID)-1,P_ID[Main_ID],P2_New_ID)
		if index2 >= 0:	Nprog2,Main_ID2,Max_Mass2,Next_ID2,Next_Mass2  = F.Locate_MainProg(index2,P_ID[Main_ID],P2_New_ID,P2_Npart)
		else:	Nprog2,Main_ID2,Max_Mass2  = -99,-99,-99
		#if i % 100 == 0: print index,index2,D_Npart[i]
		if index >= 0 and index2 >= 0 and D_Npart[i] > D.NPart_Lim:
			#MOD = M.Modulus(D_J[0][i],D_J[1][i],D_J[2][i])
			Angl1 = M.Angle(P_J[0][Main_ID],P_J[1][Main_ID],P_J[2][Main_ID],D_J[0][i],D_J[1][i],D_J[2][i])
			Angl2 = M.Angle(P_J[0][Main_ID],P_J[1][Main_ID],P_J[2][Main_ID],P2_J[0][Main_ID2],P2_J[1][Main_ID2],P2_J[2][Main_ID2])
			Angl3 = M.Angle(P2_J[0][Main_ID2],P2_J[1][Main_ID2],P2_J[2][Main_ID2],D_J[0][i],D_J[1][i],D_J[2][i])
						
			########
			Rand_Jx1,Rand_Jy1,Rand_Jz1 =  M.Ang_Rand(D_J[0][i],D_J[1][i],D_J[2][i],Angl1)
			Rand_Jx2,Rand_Jy2,Rand_Jz2 =  M.Ang_Rand(Rand_Jx1,Rand_Jy1,Rand_Jz1,Angl2)
			Angl4 = (M.Angle(Rand_Jx2,Rand_Jy2,Rand_Jz2,D_J[0][i],D_J[1][i],D_J[2][i]))
			#######
			Angle_1.append(Angl1)
			Angle_2.append(Angl2)
			Angle_3.append(Angl3)
			Angle_4.append(Angl4)
	return Angle_1,Angle_2,Angle_3,Angle_4
#####################################################################################
def CAngle(Jx1,Jy1,Jz1,Jx2,Jy2,Jz2,Jx3,Jy3,Jz3):
	VJx1 = Jx2-Jx1
	VJy1 = Jy2-Jy1
	VJz1 = Jz2-Jz1
	
	VJx2 = Jx3-Jx2
	VJy2 = Jy3-Jy2
	VJz2 = Jz3-Jz2
	
	Mod1 = VJx1*VJx1+VJy1*VJy1+VJz1*VJz1
	Mod2 = VJx2*VJx2+VJy2*VJy2+VJz2*VJz2
	
	PP = (VJx1*VJx2+VJy1*VJy2+VJz1*VJz2)/np.sqrt(Mod1*Mod2+1e-10)
	return PP
def CAngle3(Jx1,Jy1,Jz1,Jx2,Jy2,Jz2,Jx3,Jy3,Jz3,Jx4,Jy4,Jz4):
	VJx1 = Jx2-Jx1
	VJy1 = Jy2-Jy1
	VJz1 = Jz2-Jz1
	
	VJx2 = Jx4-Jx3
	VJy2 = Jy4-Jy3
	VJz2 = Jz4-Jz3
	
	Mod1 = VJx1*VJx1+VJy1*VJy1+VJz1*VJz1
	Mod2 = VJx2*VJx2+VJy2*VJy2+VJz2*VJz2
	
	PP = (VJx1*VJx2+VJy1*VJy2+VJz1*VJz2)/np.sqrt(Mod1*Mod2+1e-10)
	return PP
def Dot(Jx1,Jy1,Jz1,Jx2,Jy2,Jz2):
	Mod1 = Jx1*Jx1+Jy1*Jy1+Jz1*Jz1
	Mod2 = Jx2*Jx2+Jy2*Jy2+Jz2*Jz2
	PP = (Jx1*Jx2+Jy1*Jy2+Jz1*Jz2)/np.sqrt(Mod1*Mod2+1e-10)
	return PP
def String_Array(A):
	String = ''
	for i in range(len(A)):	String += str(M.AMedian(A[i]))+"	"
	return String

def Get_Random_J(J,Mass):
	Jr = np.zeros((len(J),len(J[0]),len(J[0][0])))-99
	Jr[D.Init_Snap-D.End_Snap] = J[D.Init_Snap-D.End_Snap]
	for Snap in reversed(range(D.End_Snap,D.Init_Snap)):
		Snap2 = Snap - D.End_Snap 
		Sel_ID = np.where((Mass[Snap2] > 0) & (J[Snap2][:,0] != -99))
		ModA2 = J[Snap2][:,0]**2 +J[Snap2][:,1]**2 +J[Snap2][:,2]**2
		ModB2 = J[Snap2+1][:,0]**2 +J[Snap2+1][:,1]**2 +J[Snap2+1][:,2]**2
		Alpha = np.arccos(np.einsum('ij,ij->i',J[Snap2],J[Snap2+1])/np.sqrt(ModA2*ModB2))
		for i in Sel_ID[0]:
			Jr[Snap2][i] = M.Ang_Rand(Jr[Snap2+1][i][0],Jr[Snap2+1][i][1],Jr[Snap2+1][i][2],Alpha[i])
		#print Snap,'\r'
	return Jr		
		
def Neg_Mass_Status(Mass,Crit = 1):
	Pre_Status = np.zeros((len(Mass),len(Mass[0])),dtype=bool)
	Pre_Status[D.Init_Snap-D.End_Snap] = np.zeros(len(Mass[0]),dtype=bool)+True
	for Snap in reversed(range(D.End_Snap,D.Init_Snap)):
		Snap2 = Snap - D.End_Snap 
		Pre_Status[Snap2] = (Mass[Snap2+1]*Crit >= Mass[Snap2]) & (Mass[Snap2] > 0)
		#all(E, axis= 0)
	return Pre_Status


def Abs_ChangeJ(J,Mass,INSnap,time,Jump2Mill = False,Cosmic_Web = -1, Web = [],WebID = -2):#D.LSnap[Id+1]
	##
	if Jump2Mill:	F = open("Data_Track/Abs_ChangeJ_MillTime_"+str(INSnap)+".ser", "w")
	else:	F = open("Data_Track/Abs_ChangeJ_"+str(INSnap)+".ser", "w")
	print >>F, "# Time	Dir_FullData	Dir_FullData_dM1	Dir_FullData_dM2	Dir_FullData_d3	Dir_FullData_dM4	Dir_FullData_dM5	"
	##
	Dir = []
	Dir_M = []
	dm = []
	for i in range(len(D.DM)-1):	Dir_M.append([])
	##
	Snap  = INSnap -1
	Sel_ID = np.where(Mass[INSnap - D.End_Snap] > 0)
	id_InMill2 = np.where(np.array(D.LSnap) == INSnap)[0][0]-1
	##
	ModA2 = J[INSnap - D.End_Snap][Sel_ID][:,0]**2 +J[INSnap - D.End_Snap][Sel_ID][:,1]**2 +J[INSnap - D.End_Snap][Sel_ID][:,2]**2  
	while True:
		if not Jump2Mill:	Snap+=1
		else:
			id_InMill2 += 1
			Snap = D.LSnap[id_InMill2]
		Snap2 = Snap - D.End_Snap 
		ModB2 = J[Snap2][Sel_ID][:,0]**2 +J[Snap2][Sel_ID][:,1]**2 +J[Snap2][Sel_ID][:,2]**2 
		Dir = np.einsum('ij,ij->i',J[INSnap - D.End_Snap][Sel_ID],J[Snap2][Sel_ID])/np.sqrt(ModA2*ModB2)
		for j in range(1,len(D.DM)):
			dm = np.where((Mass[INSnap - D.End_Snap][Sel_ID] > D.DM[j-1]) & (Mass[INSnap - D.End_Snap][Sel_ID] < D.DM[j]))
			Dir_M[j-1] = Dir[dm]
			print 'In dm ',j-1,len(Dir_M[j-1])
		print 'Total Gal = ',len(Dir)
		#DM1 = np.where((Mass[Snap2][i] < D.DM[j]) & (Mass[Snap2][i] < D.DM[j]))
		#DM1 = np.where((Mass[Snap2][i] < D.DM[j]) & (Mass[Snap2][i] < D.DM[j]))(t
	#while True:
		#Dir = []
		#if not Jump2Mill:	Snap+=1
		#else:
			#id_InMill2 += 1
			#Snap = D.LSnap[id_InMill2]
		#Snap2 = Snap - D.End_Snap 
		#for i in Sel_ID[0]:
			#for j in range(1,len(D.DM)):
				#dm = len(D.DM) - 1
				#if Mass[Snap2][i] < D.DM[j]:
					#dm = j - 1
					#break
			#Dir.append(      Dot(J[INSnap - D.End_Snap][i][0],J[INSnap - D.End_Snap][i][1],J[INSnap - D.End_Snap][i][2],J[Snap2][i][0],J[Snap2][i][1],J[Snap2][i][2]))
			#Dir_M[dm].append(Dot(J[INSnap - D.End_Snap][i][0],J[INSnap - D.End_Snap][i][1],J[INSnap - D.End_Snap][i][2],J[Snap2][i][0],J[Snap2][i][1],J[Snap2][i][2]))
		print >>F,  time[Snap],M.AMedian(Dir),String_Array(Dir_M)
		#print time[Snap],M.AMedian(Dir),String_Array(Dir_M),len(Dir)
		if Snap == D.Init_Snap:	break


	
def Abs_ChangeJ_Full(J,Jr,Mass,INSnap,time,Jump2Mill = False,Cosmic_Web = -1, Web = [],WebID = -2,ExtraName = ''):#D.LSnap[Id+1]
	##
	if ExtraName != '':	ExtraName = '_'+ExtraName
	if Jump2Mill:
		F1 = open("Data_Track/ChangeJ"+ExtraName+"_MillTime_"+str(INSnap)+".ser", "w")
		F2 = open("Data_Track/ChangeDirMillTime"+ExtraName+"_"+str(INSnap)+".ser", "w")
		F3 = open("Data_Track/Jratio"+ExtraName+"_MillTime_"+str(INSnap)+".ser", "w")
		FR1 = open("Data_Track/ChangeJ"+ExtraName+"_R_MillTime_"+str(INSnap)+".ser", "w")
		FR2 = open("Data_Track/ChangeDir"+ExtraName+"_R_MillTime_"+str(INSnap)+".ser", "w")
	else:
		F1 = open("Data_Track/ChangeJ"+ExtraName+"_"+str(INSnap)+".ser", "w")
		F2 = open("Data_Track/ChangeDir"+ExtraName+"_"+str(INSnap)+".ser", "w")
		F3 = open("Data_Track/Jratio"+ExtraName+"_"+str(INSnap)+".ser", "w")
		FR1 = open("Data_Track/ChangeJ"+ExtraName+"_R_"+str(INSnap)+".ser", "w")
		FR2 = open("Data_Track/ChangeDir"+ExtraName+"_R_"+str(INSnap)+".ser", "w")
		
	print >>F1, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	print >>F2, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	print >>F3, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	print >>FR1, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	print >>FR2, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	##
	Dir1 = []
	Dir1_M = []
	Dir2 = []
	Dir2_M = []
	Dir3 = []
	Dir3_M = []
	Dir1r = []
	Dir1r_M = []
	Dir2r = []
	Dir2r_M = []
	for i in range(len(D.DM)-1):
		Dir1_M.append([])
		Dir2_M.append([])
		Dir3_M.append([])
		Dir1r_M.append([])
		Dir2r_M.append([])
	##
	Snap  = INSnap -1
	Sel_ID = np.where(Mass[INSnap - D.End_Snap] > 0)
	id_InMill0 = np.where(np.array(D.LSnap) == INSnap)[0][0]
	id_InMill2 = id_InMill0-1
	##
	#if not Jump2Mill:	First_Vector = 
		
	ModA2 = J[INSnap - D.End_Snap][Sel_ID][:,0]**2 +J[INSnap - D.End_Snap][Sel_ID][:,1]**2 +J[INSnap - D.End_Snap][Sel_ID][:,2]**2 
	ModAR2 = Jr[INSnap - D.End_Snap][Sel_ID][:,0]**2 +Jr[INSnap - D.End_Snap][Sel_ID][:,1]**2 +Jr[INSnap - D.End_Snap][Sel_ID][:,2]**2  
	
	if not Jump2Mill:
		Snap_1 = INSnap - D.End_Snap
		Snap_2 = INSnap - D.End_Snap + 1
		
	else:
		Snap_1 = INSnap - D.End_Snap
		Snap_2 = D.LSnap[id_InMill0 + 1]
	V_diff1 = J[Snap_2][Sel_ID]-J[Snap_1][Sel_ID]
	Vr_diff1 = Jr[Snap_2][Sel_ID]-Jr[Snap_1][Sel_ID]
	Mod_diff1 = V_diff1[:,0]**2 +V_diff1[:,1]**2 +V_diff1[:,2]**2 
	Mod_rdiff1 = Vr_diff1[:,0]**2 +Vr_diff1[:,1]**2 +Vr_diff1[:,2]**2  
	##
	
	while True:
		if not Jump2Mill:	Snap+=1
		else:
			id_InMill2 += 1
			Snap = D.LSnap[id_InMill2]
		Snap2 = Snap - D.End_Snap 
		
		ModB2 = J[Snap2][Sel_ID][:,0]**2 +J[Snap2][Sel_ID][:,1]**2 +J[Snap2][Sel_ID][:,2]**2 
		ModBR2 = Jr[Snap2][Sel_ID][:,0]**2 +Jr[Snap2][Sel_ID][:,1]**2 +Jr[Snap2][Sel_ID][:,2]**2
		
		Dir1 = np.einsum('ij,ij->i',J[INSnap - D.End_Snap][Sel_ID],J[Snap2][Sel_ID])/np.sqrt(ModA2*ModB2)
		Dir1r = np.einsum('ij,ij->i',Jr[INSnap - D.End_Snap][Sel_ID],Jr[Snap2][Sel_ID])/np.sqrt(ModAR2*ModBR2)
		Dir3 = np.arccos(Dir1)/np.arccos(Dir1r)
		
		if INSnap != Snap:
			if not Jump2Mill:	Snap_3 = Snap2 - 1
			else:	Snap_3 = D.LSnap[id_InMill2 - 1]
			Snap_4 = Snap2
			
			V_diff2 = J[Snap_4][Sel_ID]-J[Snap_3][Sel_ID]
			Vr_diff2 = Jr[Snap_4][Sel_ID]-Jr[Snap_3][Sel_ID]
			Mod_diff2 = V_diff2[:,0]**2 +V_diff2[:,1]**2 +V_diff2[:,2]**2 
			Mod_rdiff2 = Vr_diff2[:,0]**2 +Vr_diff2[:,1]**2 +Vr_diff2[:,2]**2	
			Dir2 = np.einsum('ij,ij->i',V_diff1,V_diff2)/np.sqrt(Mod_diff1*Mod_diff2)
			Dir2r = np.einsum('ij,ij->i',Vr_diff1,Vr_diff2)/np.sqrt(Mod_rdiff1*Mod_rdiff2)
		for j in range(1,len(D.DM)):
			dm = np.where((Mass[INSnap - D.End_Snap][Sel_ID] > D.DM[j-1]) & (Mass[INSnap - D.End_Snap][Sel_ID] < D.DM[j]))
			Dir1_M[j-1]  = Dir1[dm]
			Dir3_M[j-1]  = Dir3[dm]
			Dir1r_M[j-1] = Dir1r[dm]
			if INSnap != Snap:
				Dir2_M[j-1]  = Dir2[dm]
				Dir2r_M[j-1] = Dir2r[dm]
		
			
		print >>F1,   time[Snap],M.AMedian(Dir1),String_Array(Dir1_M)
		print >>F2,   time[Snap],M.AMedian(Dir2),String_Array(Dir2_M)
		print >>F3,   time[Snap],M.AMedian(Dir3),String_Array(Dir3_M)
		print >>FR1,  time[Snap],M.AMedian(Dir1r),String_Array(Dir1r_M)
		print >>FR2,  time[Snap],M.AMedian(Dir2r),String_Array(Dir2r_M)
		
		print time[Snap],M.AMedian(Dir1),String_Array(Dir1_M)
		if Snap == D.Init_Snap:	break
	
	
#def Abs_ChangeJ_Full(J,Jr,Mass,INSnap,time,Jump2Mill = False,Cosmic_Web = -1, Web = [],WebID = -2):#D.LSnap[Id+1]
	###
	#if Jump2Mill:
		#F1 = open("Data_Track/ChangeJ_MillTime_"+str(INSnap)+".ser", "w")
		#F2 = open("Data_Track/ChangeDir_MillTime_"+str(INSnap)+".ser", "w")
		#F3 = open("Data_Track/Jratio_MillTime_"+str(INSnap)+".ser", "w")
		#FR1 = open("Data_Track/ChangeJ_R_MillTime_"+str(INSnap)+".ser", "w")
		#FR2 = open("Data_Track/ChangeDir_R_MillTime_"+str(INSnap)+".ser", "w")
	#else:
		#F1 = open("Data_Track/ChangeJ_"+str(INSnap)+".ser", "w")
		#F2 = open("Data_Track/ChangeDir_"+str(INSnap)+".ser", "w")
		#F3 = open("Data_Track/Jratio_"+str(INSnap)+".ser", "w")
		#FR1 = open("Data_Track/ChangeJ_R_"+str(INSnap)+".ser", "w")
		#FR2 = open("Data_Track/ChangeDir_R_"+str(INSnap)+".ser", "w")
		
	#print >>F1, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	#print >>F2, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	#print >>F3, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	#print >>FR1, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	#print >>FR2, "# Time	alpha	alpha_dM1	alpha_dM2	alpha_dM3	alpha_dM4	alpha_dM5	"
	###
	#Dir1 = []
	#Dir1_M = []
	#Dir2 = []
	#Dir2_M = []
	#Dir3 = []
	#Dir3_M = []
	#DirR1 = []
	#DirR1_M = []
	#DirR2 = []
	#DirR2_M = []
	#for i in range(len(D.DM)-1):
		#Dir1_M.append([])
		#Dir2_M.append([])
		#Dir3_M.append([])
		#DirR1_M.append([])
		#DirR2_M.append([])
	###
	#Snap  = INSnap -1
	#Sel_ID = np.where(Mass[INSnap - D.End_Snap] > 0)
	#id_InMill0 = np.where(np.array(D.LSnap) == INSnap)[0][0]
	#id_InMill2 = id_InMill0-1
	###
	
	#while True:
		#if not Jump2Mill:	Snap+=1
		#else:
			#id_InMill2 += 1
			#Snap = D.LSnap[id_InMill2]
		#Snap2 = Snap - D.End_Snap 
		#for i in Sel_ID[0]:
			#for j in range(1,len(D.DM)):
				#dm = len(D.DM) - 1
				#if Mass[Snap2][i] < D.DM[j]:
					#dm = j - 1
					#break
			#Dir1.append(      Dot(J[INSnap - D.End_Snap][i][0],J[INSnap - D.End_Snap][i][1],J[INSnap - D.End_Snap][i][2],J[Snap2][i][0],J[Snap2][i][1],J[Snap2][i][2]))
			#Dir1_M[dm].append(Dir1[-1])
			
			#DirR1.append(      Dot(Jr[INSnap - D.End_Snap][i][0],Jr[INSnap - D.End_Snap][i][1],Jr[INSnap - D.End_Snap][i][2],Jr[Snap2][i][0],Jr[Snap2][i][1],Jr[Snap2][i][2]))
			#DirR1_M[dm].append(DirR1[-1])
			
			#Dir3.append(      Dir1[-1]/DirR1[-1])
			#Dir3_M[dm].append(Dir3[-1])
			
			#if INSnap != Snap:
				#if not Jump2Mill:
					#Snap_1 = INSnap - D.End_Snap
					#Snap_2 = INSnap - D.End_Snap + 1 
					#Snap_3 = Snap2 - 1
					#Snap_4 = Snap2 
				#else:
					#Snap_1 = INSnap - D.End_Snap
					#Snap_2 = D.LSnap[id_InMill0 + 1]
					#Snap_3 = D.LSnap[id_InMill2 - 1]
					#Snap_4 = Snap2
				#Dir2.append(      CAngle3(J[INSnap - D.End_Snap][i][0],J[INSnap - D.End_Snap][i][1],J[INSnap - D.End_Snap][i][2],J[Snap2][i][0],J[Snap2][i][1],J[Snap2][i][2]))
				#Dir2_M[dm].append(Dir2[-1])
			
			
		#print >>F,  time[Snap],M.AMedian(Dir),String_Array(Dir_M)
		#if Snap == D.Init_Snap:	break