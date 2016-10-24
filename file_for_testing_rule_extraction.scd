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
//            import and use unify rules function
//
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"/home/ivan/documents/in-construction/unification_of_rules.scd".load;
~unify_rules = ~unification_of_rules.value(~bag,~intervals_and_distances);
~unify_rules.do{|x,i| i.post; x.postln}










