//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
//               script to eliminate the
//                    redundant rules
//         comming from different compaction orders
//%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
//(~rules = [
//	[10, [20,88], 1],
//	[10, [16,20,28,88], 1]  ])

(~redundant_rules = {
arg rules;
var indexes; var result = [];
var newIntervals, deleteIndexes = [];
var temporalRules = rules.deepCopy;///////
indexes = (0 .. rules[0].size - 2);
indexes.collect{ arg colToExclude;
//var temporalRules = rules;
var section, subsets, selection;
var temporal = [];
section = (0.. indexes.size).removing(colToExclude);
subsets = temporalRules.slice(nil,section);
selection = temporalRules.slice(nil,colToExclude);
subsets.do{ arg row, i;
	var values = [], indexes = [];
	//'row : '.post; row.postln;
	values = values.add(selection[i]);indexes=indexes.add(i);
	subsets.do{ arg row1, j;
		if((row==row1) && (i!=j)){
			if(row1.notNil){
				values = values.add(selection[j]);
				indexes = indexes.add(j)};
			}};
			if(values.size>1){
				'indexes'.post;indexes.post;values.postln;
				deleteIndexes = ~content.value(values,indexes)
			}
		};
		deleteIndexes.collect({arg index; temporalRules[index]=nil});
	};
	temporalRules
});
//~redundant_rules.value(~rules);

(~content = {arg values, indexes;
	var dictionaries = [];
	var deleteIndexes = [];
	values.do{ arg x, i;
		var dict = Dictionary.new;
		var set = Set.new, index;
		x.postln;
		x.do{|element| set = set.add(element)};
		dict.add('set' -> set);
		dict.add('id'-> i.asString);
		dictionaries = dictionaries.add(dict)
	};
	dictionaries.postln;
	dictionaries.do{arg x, i;
		dictionaries.do{arg y, j;
			if(
				( ( x.at('set') & y.at('set') ) == x.at('set') ) &&
				(i!=j)
			){
				x.at('set').postln;
				deleteIndexes = deleteIndexes.add(indexes[i])
			}
			}};
		deleteIndexes
});
//~content.value( [ [20,88], [16,20,28,88] ], [0,1] )
