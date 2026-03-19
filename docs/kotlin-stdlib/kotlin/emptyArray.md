

# emptyArray

Returns an empty array of the specified type T.

```kotlin
expect fun <T> emptyArray(): Array<T>(source)
```

```kotlin
val emptyStrings: Array<String> = emptyArray()
println("Size: ${emptyStrings.size}")          // 0

// Adding elements to a new array
val greetings = arrayOf("Hello", "Hi", "Hey")
val combined = greetings + emptyStrings        // same as greetings

println("Combined size: ${combined.size}")     // 3
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/empty-array.html)

    