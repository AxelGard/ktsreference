

# mapNotNull

Returns a list containing only the non-null results of applying the given transform function to each element in the original array.

```kotlin
inline fun <T, R : Any> Array<out T>.mapNotNull(transform: (T) -> R?): List<R>(source)
```

```kotlin
val words = arrayOf("12", "hello", "34", "world")

val numbers = words.mapNotNull { word ->
    word.toIntOrNull()   // returns null if the word is not a number
}

println(numbers)   // prints: [12, 34]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-not-null.html)

    