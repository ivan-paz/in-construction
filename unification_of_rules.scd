//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//                    script for
//              unification of rules
//
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(
//  data set for proves
(~rules = [
	[3,   [33, 659], 1],
	[100, [33, 659], 1],
	[3,   [21, 33],  1],
	[2,   300,       1]
]);
~intervals_and_distances = [
      [

              [ [0, inf], 1000]

      ],

      [

              [ [0,inf], 1000 ]
      ]
]
)
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(~unification_of_rules = {
arg rules, intervals_and_distances;
var indexes;
indexes = (0 .. rules[0].size - 2);
indexes.collect{ arg colToExclude;
	var temporalRules = rules.deepCopy;
	var section, subsets, selection;
	section = (0.. indexes.size).removing(colToExclude);
	subsets = temporalRules.slice(nil,section);
	selection = temporalRules.slice(nil,colToExclude);
	subsets.do{arg row,i;
		'row: '.post; row.postln;
		subsets.do{arg row1,j;
			var values = [];
		if(row==row1&&i!=j){
			values = values.add(selection[i]);
			'row1: '.post;row1.postln;
		};
		values.postln;
		}
	}
}
})
~unification_of_rules.value(~rules,~intervals_and_distances);
