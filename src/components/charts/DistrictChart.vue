<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { computed, defineProps, ref } from "vue";
import { useMapStore } from "../../store/mapStore";
import { useDialogStore } from "../../store/dialogStore";
import { districtCoordinates } from "../../assets/configs/apexcharts/districtCoordinates";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
	"map_filter",
]);
const mapStore = useMapStore();
const dialogStore = useDialogStore();

const targetDistrict = ref(null);
const districtColor = ref(props.chart_config.color[0]);
const mousePosition = ref({ x: null, y: null });
const selectedIndex = ref(null);
const districts = [
	"北投區",
	"士林區",
	"內湖區",
	"南港區",
	"松山區",
	"信義區",
	"中山區",
	"大同區",
	"中正區",
	"萬華區",
	"大安區",
	"文山區",
	"桃園區",
	"八德區",
	"大園區",
	"大溪區",
	"中壢區",
	"平鎮區",
	"復興區",
	"新屋區",
	"楊梅區",
	"龍潭區",
	"龜山區",
	"蘆竹區",
	"觀音區"

];

// Parse District Data (to support 2D or 3D data)
const districtData = computed(() => {
	let output = {};
	let highest = 0;
	let sum = 0;
	if (props.series.length === 1) {
		props.series[0].data.forEach((item) => {
			output[item.x] = item.y;
			if (item.y > highest) {
				highest = item.y;
			}
			sum += item.y;
		});
	} else {
		props.series.forEach((serie) => {
			for (let i = 0; i < 12; i++) {
				if (!output[props.chart_config.categories[i]]) {
					output[props.chart_config.categories[i]] = 0;
				}
				output[props.chart_config.categories[i]] += +serie.data[i];
			}
		});
		highest = Object.values(output).sort(function (a, b) {
			return b - a;
		})[0];
		sum = Object.values(output).reduce(
			(partialSum, a) => partialSum + a,
			0
		);
	}

	output.highest = highest;
	output.sum = sum;
	return output;
});
const tooltipPosition = computed(() => {
	return {
		left: `${mousePosition.value.x - 10}px`,
		top: `${mousePosition.value.y - 54}px`,
	};
});

function toggleActive(e) {
	targetDistrict.value = e.target.dataset.name;
}
function toggleActiveToNull() {
	targetDistrict.value = null;
}
function updateMouseLocation(e) {
	mousePosition.value.x = e.pageX;
	mousePosition.value.y = e.pageY;
}

function handleDataSelection(index) {
	if (!props.map_filter) {
		return;
	}
	if (index !== selectedIndex.value) {
		if (mapStore.map && !dialogStore.dialogs.moreInfo) {
			mapStore.flyToLocation(districtCoordinates[index]);
		}
		// Supports filtering by xAxis
		if (props.map_filter.mode === "byParam") {
			mapStore.filterByParam(
				props.map_filter,
				props.map_config,
				districts[index]
			);
		}
		// Supports filtering by xAxis
		else if (props.map_filter.mode === "byLayer") {
			mapStore.filterByLayer(props.map_config, districts[index]);
		}
		selectedIndex.value = index;
	} else {
		if (mapStore.map && !dialogStore.dialogs.moreInfo) {
			mapStore.flyToLocation([121.536609, 25.044808]);
		}
		if (props.map_filter.mode === "byParam") {
			mapStore.clearByParamFilter(props.map_config);
		} else if (props.map_filter.mode === "byLayer") {
			mapStore.clearByLayerFilter(props.map_config);
		}
		selectedIndex.value = null;
	}
}
</script>

<template>
	<div v-if="activeChart === 'DistrictChart'" class="districtchart">
		<div class="districtchart-title">
			<h5>{{ chart_config.tittle_2 }}  </h5>
			<h6>{{ chart_config.text }} {{ chart_config.unit }}</h6>

			<div class="districtchart-title-legend">
				<p>{{ chart_config.tittle_3 }}</p>
				<div
					:style="{ backgroundColor: props.chart_config.color[0] }"
				></div>
				<p>{{ chart_config.tittle_4 }}</p>
			</div>
		</div>
		<div class="districtchart-chart">
			<svg viewBox="0 0 1980 1080" height="400" width="500" xmlns="http://www.w3.org/2000/svg">
				<g transform=" translate(-1000, -1000) scale(2.2)">
					<path
						data-name="蘆竹區"
						:class="{
							'active-district':
								targetDistrict === '蘆竹區' ||
								selectedIndex === 33,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(33)"
						:fill-opacity="
							districtData['蘆竹區'] / districtData.highest
						"
						:fill="districtColor"
						d="M960,16.765L1014.804,26L1031,44l20.5,11.289l15.449,9.064c0,0,29.817,0.353,29.434,0
						C1096,64,1142.837,89,1142.837,89L1099,144h-21.879H1059l-7.581,7.597v31.725L1040,183l-11.6,9.84L1014,183l-17.325,30L992,257.116
						l-17,6.652l-47.5-89.51L946,158l-7-6l26-17.399l37-19.262l-37-72.515L960,16.765z"
					
					/>
			
				
					<path
						data-name="大園區"
						:class="{
							'active-district':
								targetDistrict === '大園區' ||
								selectedIndex === 23,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(23)"
						:fill-opacity="
							districtData['大園區'] / districtData.highest
						"
						:fill="districtColor"
						d="M760,89 L534,203 L585,224 L647,245.639 L677,268 L710,257 L720,262 L717,278 L749,314 L781,282 L781,272.832 
						787,249 L759,221 L772,171 L772,156 L764,139 L767,118 Z"
					/>
					
					<path
						data-name="觀音區"
						:class="{
							'active-district':
								targetDistrict === '觀音區' ||
								selectedIndex === 21,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(21)"
						:fill-opacity="
							districtData['觀音區'] / districtData.highest
						"
						:fill="districtColor"
						d="M766.668,89 L946,26 L992,115 L951,136 L939,152 L939,161 L927.5,174.258 L949,220 L927.5,233.176 L901,207 
	886.77,233.176 L879.334,225.245 L879.334,208.249 L861,191 L840,208 L828.985,201.5 L766.668,186.721 L781,166 L764,139 L773,112 Z"
						
					/>
					<path
						data-name="新屋區"
						:class="{
							'active-district':
								targetDistrict === '新屋區' ||
								selectedIndex === 22,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(22)"
						:fill-opacity="
							districtData['新屋區'] / districtData.highest
						"
						:fill="districtColor"
						d="M526,213 L506,232 L499,260 L504,277 L460,342 L567,371 L605,350 L619,345 L642,332 L673,350 L709,345 L722,337 
						754,336 L759,332 L709,275 L713,266 L699.486,260.505 L677,268 L647,245.639 Z"
					/>
					<path
						data-name="楊梅區"
						:class="{
							'active-district':
								targetDistrict === '楊梅區' ||
								selectedIndex === 30,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(30)"
						:fill-opacity="
							districtData['楊梅區'] / districtData.highest
						"
						:fill="districtColor"
						d="M581.982,371 L581.982,434.857 L638,451 L677,459 L688,475 L759,483.578 L795,499 L834,475 L834,430.325 
	834,396.334 L805,329 L787,338.549 L759,332 L743,344 L722,337 L683,357 L650.089,336.697 L630.036,338.762 Z"
					/>
					<path
						data-name="中壢區"
						:class="{
							'active-district':
								targetDistrict === '中壢區' ||
								selectedIndex === 26,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(26)"
						:fill-opacity="
							districtData['中壢區'] / districtData.highest
						"
						:fill="districtColor"
						d="M766.322,192.84 L766.322,218.446 L794,251 L787,272.832 L787,286.429 L769.92,293.08 L771.2,309 L759,314 
	764,323.819 L794,323.819 L815,301 L834,303.424 L848.247,329 L861.843,329 L909,359 L912.508,381.374 L951.353,394.5 L1002,337 
	949,220 L915,243 L904,221 L878,237.708 L868.642,201.5 L852.031,198.261 L841.449,213 L828.985,201.5 L816.522,201.5 Z"
					/>


					<path
						data-name="桃園區"
						:class="{
							'active-district':
								targetDistrict === '桃園區' ||
								selectedIndex === 24,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(24)"
						:fill-opacity="
							districtData['桃園區'] / districtData.highest
						"
						:fill="districtColor"
						d="M1019.336,192.84 L996.675,213 L996.675,250.171 L984,269 L984,284.163 L1007,284 L1019.336,272.832 
	1041.997,314 L1052,285 L1079.387,293.67 L1100,283 L1119,223 L1089.584,192.84 L1082,175 L1062,180 L1051.5,192.84 L1036.332,192.84 Z"
					/>
					<path
						data-name="龜山區"
						:class="{
							'active-district':
								targetDistrict === '龜山區' ||
								selectedIndex === 28,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(28)"
						:fill-opacity="
							districtData['龜山區'] / districtData.highest
						"
						:fill="districtColor"
						d="M1059,165 L1059,153.863 L1078.254,153.863 L1099,144 L1146,106 L1161,119 L1223.283,135.5 L1233,154 L1243,150 
	1243,175 L1269.738,213 L1243,225 L1261.807,244.5 L1223,265 L1221,280 L1114.511,280 L1125,226 L1100.915,192.84 L1087.147,187.106 
	1088.451,175 Z"
					/>
					
					<path
						data-name="八德區"
						:class="{
							'active-district':
								targetDistrict === '八德區' ||
								selectedIndex === 29,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(29)"
						:fill-opacity="
							districtData['八德區'] / districtData.highest
						"
						:fill="districtColor"
						d="M806,319 L820,309 L834,309 L841.449,329 L854,341 L859.577,341 L898,358 L916,387 L954,400 L975,388 
	975,405.398 L960,405.398 L960,414 L955,444 L960,458.651 L954,471 L909,480 L872,472 L848,475 L834,442.788 L846,403 Z"
					/>
					<path
						data-name="平鎮區"
						:class="{
							'active-district':
								targetDistrict === '平鎮區' ||
								selectedIndex === 25,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(25)"
						:fill-opacity="
							districtData['平鎮區'] / districtData.highest
						"
						:fill="districtColor"
						d="M1002,293.67 L1010.272,329 L984,388.402 L992,398.6 L1016,390 L1059,398.6 L1119,346.135 L1104.314,293.67 
	1079.387,293.67 L1059,292 L1051.5,329 L1015.937,280 Z"
					/>

					<path
						data-name="龍潭區"
						:class="{
							'active-district':
								targetDistrict === '龍潭區' ||
								selectedIndex === 27,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(27)"
						:fill-opacity="
							districtData['龍潭區'] / districtData.highest
						"
						:fill="districtColor"
						d="M787,507.372 L787,520.968 L773,556 L853,608 L865.242,608 L878,618.41 L890.5,618.41 L927.5,625.208 
	960,610.478 L1002,540 L1002,526.633 L967,524 L984,480 L975,467.715 L943,487 L872.041,480 L840,475 L815.389,499 Z"
					/>


					<path
						data-name="大溪區"
						:class="{
							'active-district':
								targetDistrict === '大溪區' ||
								selectedIndex === 31,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(31)"
						:fill-opacity="
							districtData['大溪區'] / districtData.highest
						"
						:fill="districtColor"
						d="M965,442 L979.68,414 L1017.07,398.6 L1051.5,406.531 L1074.403,385.131 L1092.984,398.6 L1119,398.6 
	1085.052,414 L1096,428 L1096,456 L1125.842,467.715 L1146.236,499 L1164.369,505.106 L1152,514 L1168.897,540 L1139,552 L1153,572 
	1125,615 L1077.121,615 L1041,609 L996.675,615 L969.482,625.208 L992,566.29 L1015,531 L1002,516.436 L975,519.835 L992,484.711 Z"/>
				
					/>
					<path
						data-name="復興區"
						:class="{
							'active-district':
								targetDistrict === '復興區' ||
								selectedIndex === 32,
							'initial-animation-12': true,
						}"
						@mouseenter="toggleActive"
						@mousemove="updateMouseLocation"
						@mouseleave="toggleActiveToNull"
						@click="handleDataSelection(32)"
						:fill-opacity="
							districtData['復興區'] / districtData.highest
						"
						:fill="districtColor"
						d="M965,639.937 L992,679.594 L1081,731 L1074,757 L1073,782 L1086,802 L1073,851 L1099,838 L1153,868 
	1153,896.005 L1178,911 L1178,963.987 L1199,976 L1199,1024.038 L1221,1050 L1269.738,1050 L1298,1034 L1364,1038 L1382,1003 L1417,967 
	1393,915 L1407,886 L1407,850 L1351,825 L1311,718 L1357,675 L1335,656 L1330.922,625.208 L1286,587 L1269.738,558.358 L1213,581 
	1164.369,565.157 L1127,620 L1078,625 L1039,616 L1002,614.279 Z"
					/>
				</g>
			</svg>
			<Teleport to="body">
				<!-- The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css -->
				<div
					v-if="targetDistrict"
					class="districtchart-chart-info chart-tooltip"
					:style="tooltipPosition"
				>
					<h6>{{ targetDistrict }}</h6>
					<span
						>{{ districtData[targetDistrict] }}
						{{ chart_config.unit }}</span
					>
				</div>
			</Teleport>
		</div>
	</div>
</template>

<style scoped lang="scss">
.districtchart {
	max-height: 100%;
	position: relative;
	overflow-y: scroll;

	&-title {
		display: flex;
		flex-direction: column;
		justify-content: center;
		position: absolute;
		left: 0;
		top: 0;
		margin: 0.5rem 0 -0.5rem;

		h5 {
			color: var(--color-complement-text);
		}

		h6 {
			color: var(--color-complement-text);
			font-size: var(--font-m);
			font-weight: 400;
		}

		&-legend {
			display: flex;
			justify-content: space-between;

			div {
				position: relative;
				width: 3rem;
				margin: 0 4px;
				border-radius: 5px;
			}

			div:before {
				content: "";
				width: 3rem;
				height: var(--font-l);
				position: absolute;
				top: 0;
				left: 0;
				background: linear-gradient(
					270deg,
					rgb(40, 42, 44,1),
					rgba(50, 73, 163, 0.2)
				);
			}

			p {
				color: var(--color-complement-text);
			}
		}
	}

	&-chart {
		display: flex;
		justify-content: center;

		svg {
			width: 50%;

			path {
				transition: transform 0.2s;
				opacity: 0;
			}
		}

		&-info {
			position: fixed;
			z-index: 20;
		}
	}
}

.active-district {
	transform: translateY(-10px);
}

@keyframes ease-in {
	0% {
		opacity: 0;
	}

	100% {
		opacity: 1;
	}
}

@for $i from 1 through 12 {
	.initial-animation-#{$i} {
		animation-name: ease-in;
		animation-duration: 0.2s;
		animation-delay: 0.05s * ($i - 1);
		animation-timing-function: linear;
		animation-fill-mode: forwards;
	}
}
</style>
