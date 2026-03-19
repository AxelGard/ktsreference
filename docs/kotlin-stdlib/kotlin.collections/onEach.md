

# onEach

Performs the given action on each element and returns the array itself afterwards.

```kotlin
inline fun <T> Array<out T>.onEach(action: (T) -> Unit): Array<out T>(source)
```

```kotlin
val fruits = arrayOf("Apple", "Banana", "Cherry")

// Perform an action on each element and get the original array back
val sameArray = fruits.onEach { println("Processing: $it") }

// The returned array is the same instance as `fruits`
println(sameArray.contentToString())  // [Apple, Banana, Cherry]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/on-each.html)

    