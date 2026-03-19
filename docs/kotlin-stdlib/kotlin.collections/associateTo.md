

# associateTo

Populates and returns the destination mutable map with key-value pairs provided by transform function applied to each element of the given array.

```kotlin
@IgnorableReturnValueinline fun <T, K, V, M : MutableMap<in K, in V>> Array<out T>.associateTo(destination: M, transform: (T) -> Pair<K, V>): M(source)
```

val fruits = arrayOf("apple", "banana", "cherry")
val lengths = mutableMapOf<String, Int>()
fruits.associateTo(lengths) { it to it.length }

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate-to.html)

    