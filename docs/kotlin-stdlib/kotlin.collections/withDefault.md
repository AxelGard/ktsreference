

# withDefault

Returns a wrapper of this read-only map, having the implicit default value provided with the specified function defaultValue.

```kotlin
fun <K, V> Map<K, V>.withDefault(defaultValue: (key: K) -> V): Map<K, V>(source)
```

```kotlin
val map = mapOf(1 to "one", 2 to "two")
val mapWithDefault = map.withDefault { key -> "missing key $key" }

println(mapWithDefault[1])   // prints: one
println(mapWithDefault[3])   // prints: missing key 3
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/with-default.html)

    