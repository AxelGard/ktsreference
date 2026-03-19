

# filterTo

Appends all elements matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, C : MutableCollection<in T>> Array<out T>.filterTo(destination: C, predicate: (T) -> Boolean): C(source)
```

```kotlin
val words = arrayOf("apple", "banana", "avocado", "cherry")
val aWords = mutableListOf<String>()

words.filterTo(aWords) { it.startsWith("a") }

println(aWords)  // [apple, avocado]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-to.html)

    