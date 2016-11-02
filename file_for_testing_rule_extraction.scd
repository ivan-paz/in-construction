//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//                file for test
//            rule extraction function
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

"/home/ivan/documents/in-construction/rule_extraction_function.scd".load;


//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
//                 Load Files
//                and create data
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

//               Intervals and distances
(
(~intervals_and_distances = [
	[
	[ [0, inf], 1000 ]
	//[ [0, 15], 5], [ [15,55], 10], [ [55,inf], 500]
],
[
	[ [0,inf], 1000 ]
]
]);
(      // load X, y train
x = CSVFileReader.readInterpret("/home/ivan/documents/in-construction/X_train_0.csv");
y = CSVFileReader.readInterpret("/home/ivan/documents/in-construction/y_train_0.csv");
);
       //   data
(
~data = [];
x.do{arg x, i;
	x = x.add(y[i][0]);
	~data = ~data.add(x);
});
)

//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
//                   compression process
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
(
~rules = ~subsetsCompression.value(~data,~intervals_and_distances);
~bag = ~bagOfRules_uncompleted.value(~rules);
);
~bag.do{ arg instance, i; i.post;instance.postln};
//-------         write rules into csv file       -------------
(
f = File("/home/ivan/documents/in-construction/report/rules.csv","w");
~bag.do{arg rule, i;
	f.write(i + "," + rule + "\n");
};
f.close
)


//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//            Eliminate the redundant rules
//
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

"/home/ivan/documents/in-construction/redundant_rules.scd".load;
(
~new_rules  = ~redundant_rules.value(~bag);
~new_rules.do{|x,i| i.post; x.postln};
///////------------------------------------***
~non_redundant = [ ];
~new_rules.collect({|x|
if(x.notNil){~non_redundant = ~non_redundant.add(x)}})
)

~non_redundant.do{|x,i| [ i, x ].postln}

//&&&&&&&&&&&&&&&&&   write file &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(f = File("/home/ivan/documents/in-construction/report/non_redundant_rules.csv","w");
~non_redundant.do{arg rule, i; f.write(i + "," + rule + "\n")};f.close)


//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//                   Unification of intervals
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"/home/ivan/documents/in-construction/unification_of_rules.scd".load

~unified_rules = ~unification_of_rules.value(~non_redundant,~intervals_and_distances)

~unified_rules.do{|x,i| [i,x].postln};
//&&&&&&&&&&&&&&&&&     write a file      &&&&&&&&&&&&&&&&&&&&&&
(
f = File("/home/ivan/documents/in-construction/report/unified_rules.csv","w");
~unified_rules.do{arg rule, i;f.write(i + "," + rule + "\n")};f.close
)















