

# getOrPut

Returns the value for the given key if the value is present and not null. Otherwise, calls the defaultValue function, puts its result into the map under the given key and returns the call result.

```kotlin
inline fun <K, V> MutableMap<K, V>.getOrPut(key: K, defaultValue: () -> V): V(source)
```

```kotlin
val map = mutableMapOf<String, Int>()

// The key "apple" is not in the map yet, so the default lambda is called
val count1 = map.getOrPut("apple") { 0 }
println(count1)          // prints 0
println(map["apple"])    // prints 0

// The key "apple" is already present, so the lambda is not executed
val count2 = map.getOrPut("apple") { 10 }
println(count2)          // prints 0

// Updating the value manually
map["apple"] = 5
println(map.getOrPut("apple") { 10 })  // prints 5
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get-or-put.html)

    