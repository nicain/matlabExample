function matlabExample(jobIndex)

	% Change jobIndex to a number
    jobIndex = str2num(jobIndex);
	
	% Set up parameter space:
    A=linspace(0,10,3);
    B=linspace(15,115,3);
    C=linspace(95,111,3);

    % Use setProd, another matlab file, to construct parameter space:
    paramSpace = setprod(A,B,C);
    
    % Run for a single element:
    coreAlgorithm(paramSpace(jobIndex,1),paramSpace(jobIndex,2),paramSpace(jobIndex,3))
    
	exit
return

function coreAlgorithm(A,B,C)
% This is the function to be run at each element of param space

    % Nothing too fancy!
    myOutputVar=A+B+C;
    pause(2)
    
    disp(['saveFile_',num2str(A),'_',num2str(B),'_',num2str(C),'.dat'])
    
    % Save the output:
    save(['saveFile_',num2str(A),'_',num2str(B),'_',num2str(C),'.dat'],'myOutputVar','-ascii')
    
return