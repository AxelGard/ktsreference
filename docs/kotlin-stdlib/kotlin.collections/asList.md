

# asList

Returns a List that wraps the original array.

```kotlin
expect fun <T> Array<out T>.asList(): List<T>(source)
```

```kotlin
val array = arrayOf("apple", "banana", "cherry")

val list: List<String> = array.asList()

println(list)           // [apple, banana, cherry]
println(list[1])        // banana
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-list.html)

    