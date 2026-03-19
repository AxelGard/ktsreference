

# safeCast

Casts the given value to the class represented by this KClass object. Returns null if the value is null or if it is not an instance of this class.

```kotlin
fun <T : Any> KClass<T>.safeCast(value: Any?): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val value: Any = Person("Alice", 30)

    // Cast to Person
    val person: Person? = Person::class.safeCast(value)
    // Cast to String (will return null)
    val string: String? = String::class.safeCast(value)

    println(person?.name)   // prints: Alice
    println(string)         // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/safe-cast.html)

    