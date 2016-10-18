//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//                file for test
//            rule extraction function
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(
	"/home/ivan/documents/in-construction/rule_extraction_function.scd".load;
)
(~intervals_and_distances = [
	[
	[ [0, inf], 1000 ]
	//[ [0, 15], 5], [ [15,55], 10], [ [55,inf], 500]
],
[
	[ [0,inf], 1000 ]
]
]);
~data = CSVFileReader.readInterpret("/home/ivan/documents/in-construction/band_limited_impulse_oscillator_perceptual_space3.csv");
// delete observation number
(
~cleanData = [];
~data.do{arg x;
	x = x[1..];
	~cleanData = ~cleanData.add(x);
};
~cleanData = ~cleanData[1..]
)
~cleanData.do{arg x; x.postln}
//      compression process
~rules = ~subsetsCompression.value(~cleanData,~intervals_and_distances);
~bag = ~bagOfRules_uncompleted.value(~rules);
~bag.do{ arg instance, i; i.post;instance.postln}
