<map version="freeplane 1.3.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="NEAT Notes" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1437813315012"><hook NAME="MapStyle">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="12" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="1"/>
<font SIZE="12"/>
<node TEXT="Design questions" POSITION="right" ID="ID_1622282061" CREATED="1437813342255" MODIFIED="1437813345926">
<edge COLOR="#ff0000"/>
<node TEXT="What drives network?" ID="ID_830799441" CREATED="1437813346179" MODIFIED="1437813350485">
<node TEXT="e.g. pull data thru?" ID="ID_1338594679" CREATED="1437813350772" MODIFIED="1437813357270">
<node TEXT="only works (well) if you have a single output?" ID="ID_577591092" CREATED="1437813378207" MODIFIED="1437813388044"/>
<node TEXT="unless you abstract out the result?" ID="ID_20982991" CREATED="1437813394268" MODIFIED="1437813411578"/>
<node TEXT="And what about cycles?" ID="ID_1824130320" CREATED="1437846714699" MODIFIED="1437846718616"/>
<node TEXT="Can&apos;t use recursion?" ID="ID_59573340" CREATED="1437846720689" MODIFIED="1437846728081"/>
</node>
<node TEXT="or push data in?" ID="ID_1604187090" CREATED="1437813357633" MODIFIED="1437813360731"/>
<node TEXT="or external iteration over each layer in turn?" ID="ID_905787748" CREATED="1437813360937" MODIFIED="1437813376708">
<node TEXT="this is the ticket" ID="ID_1850730270" CREATED="1437939371539" MODIFIED="1437939381245">
<font BOLD="true" ITALIC="true"/>
</node>
<node TEXT="else loops will suck" ID="ID_1523985254" CREATED="1437939382143" MODIFIED="1437939388198"/>
</node>
<node TEXT="Can synapses go backwards?" ID="ID_1906031339" CREATED="1437846559959" MODIFIED="1437846588986">
<font BOLD="false" ITALIC="true"/>
</node>
</node>
<node TEXT="Representation" ID="ID_1927746111" CREATED="1437813446847" MODIFIED="1437813453148">
<node TEXT="Neurons are natural frame of the network (eg. Neuron(incoming, outgoing))" ID="ID_1775313254" CREATED="1437813453697" MODIFIED="1437813477285"/>
<node TEXT="But: Synapses are the things with innovation number and the things that get crossed/ mutated" ID="ID_1058072320" CREATED="1437813477942" MODIFIED="1437813516561"/>
<node TEXT="Adding new neurons can be represented by &apos;splitting&apos; a synapse into two" ID="ID_552191998" CREATED="1437813518405" MODIFIED="1437813539261"/>
</node>
<node TEXT="Mutations" ID="ID_697323022" CREATED="1437813553569" MODIFIED="1437813555356">
<node TEXT="Enable/ Disable synapse" ID="ID_646210749" CREATED="1437813588054" MODIFIED="1437813593541"/>
<node TEXT="" ID="ID_47836497" CREATED="1437813672824" MODIFIED="1437813672824"/>
</node>
<node TEXT="Mating" ID="ID_256000959" CREATED="1437813677107" MODIFIED="1437813681034">
<node TEXT="Crossover - matching synapses (same inno num) are randomly picked" ID="ID_1476288588" CREATED="1437813681520" MODIFIED="1437813700281"/>
<node TEXT="" ID="ID_1474157434" CREATED="1437813701993" MODIFIED="1437813701993"/>
</node>
<node TEXT="Random" ID="ID_608452999" CREATED="1437813719389" MODIFIED="1437813722818">
<node TEXT="Can we set seed to get rerunnability?" ID="ID_1742667978" CREATED="1437813723152" MODIFIED="1437813730654"/>
</node>
</node>
</node>
</map>
